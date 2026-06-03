# ── 실습본: 실제 OpenVLA 코드 그대로, ★STEP★ 부분(행동 역토큰화/역정규화)만 비움 ──
# 원본(verbatim): reference/papers/D_openvla/prismatic/extern/hf/modeling_prismatic.py
#   class OpenVLAForActionPrediction.predict_action()  (lines 506~536)
#   (Kim et al., OpenVLA, arXiv:2406.09246)
# ★VLA 핵심★: '행동'을 언어 토큰으로 취급 → 생성된 토큰을 역양자화/역정규화.
# 채운 뒤 원본 modeling_prismatic.py 와 diff 로 대조.
from typing import Dict, Any, Optional

import numpy as np
import torch
from transformers import PretrainedConfig

from prismatic.extern.hf.modeling_prismatic import PrismaticForConditionalGeneration
from prismatic.extern.hf.configuration_prismatic import OpenVLAConfig


class OpenVLAForActionPrediction(PrismaticForConditionalGeneration):
    config_class: PretrainedConfig = OpenVLAConfig

    def __init__(self, config: OpenVLAConfig) -> None:
        super().__init__(config)
        self.norm_stats = config.norm_stats

        # Compute action bins
        self.bins = np.linspace(-1, 1, config.n_action_bins)
        self.bin_centers = (self.bins[:-1] + self.bins[1:]) / 2.0

        # Compute vocab size for de-tokenization -- revert added "multiple of"
        self.vocab_size = self.config.text_config.vocab_size - self.config.pad_to_multiple_of

    def predict_action(
        self, input_ids: Optional[torch.LongTensor] = None, unnorm_key: Optional[str] = None, **kwargs: str
    ) -> np.ndarray:
        """Thin wrapper around .generate() that decodes predicted actions and unnormalizes them."""
        # If the special empty token ('') does not already appear after the colon (':') token in the prompt
        # (after "OUT:" or "ASSISTANT:"), insert it to match the inputs seen at training time
        if not torch.all(input_ids[:, -1] == 29871):
            input_ids = torch.cat(
                (input_ids, torch.unsqueeze(torch.Tensor([29871]).long(), dim=0).to(input_ids.device)), dim=1
            )

        # Run VLA inference
        generated_ids = self.generate(input_ids, max_new_tokens=self.get_action_dim(unnorm_key), **kwargs)

        # ★STEP 1★ 생성된 토큰ID → (정규화된) 연속 행동 으로 역토큰화하라:
        #   predicted_action_token_ids = generated_ids[0, -self.get_action_dim(unnorm_key):].cpu().numpy()
        #   discretized_actions = self.vocab_size - predicted_action_token_ids
        #   discretized_actions = np.clip(discretized_actions - 1, a_min=0, a_max=self.bin_centers.shape[0] - 1)
        #   normalized_actions = self.bin_centers[discretized_actions]
        raise NotImplementedError("★STEP 1★ 토큰ID → 정규화 행동 (역양자화)")

        # ★STEP 2★ 정규화 행동([-1,1]) → 실제 행동 으로 역정규화하라 (q01/q99 통계 사용):
        #   action_norm_stats = self.get_action_stats(unnorm_key)
        #   mask = action_norm_stats.get("mask", np.ones_like(action_norm_stats["q01"], dtype=bool))
        #   action_high, action_low = np.array(action_norm_stats["q99"]), np.array(action_norm_stats["q01"])
        #   actions = np.where(
        #       mask,
        #       0.5 * (normalized_actions + 1) * (action_high - action_low) + action_low,
        #       normalized_actions,
        #   )
        raise NotImplementedError("★STEP 2★ 정규화 행동 → 실제 행동 (역정규화)")

        return actions

    @staticmethod
    def _check_unnorm_key(norm_stats: Dict[str, Dict[str, Any]], unnorm_key: Optional[str]) -> str:
        if unnorm_key is None:
            assert len(norm_stats) == 1, (
                f"Your model was trained on more than one dataset, "
                f"please pass a `unnorm_key` from the following options to choose the statistics "
                f"used for un-normalizing actions: {norm_stats.keys()}"
            )
            unnorm_key = next(iter(norm_stats.keys()))

        assert unnorm_key in norm_stats, (
            f"The `unnorm_key` you chose is not in the set of available dataset statistics, "
            f"please choose from: {norm_stats.keys()}"
        )
        return unnorm_key

    def get_action_dim(self, unnorm_key: Optional[str] = None) -> int:
        """Get the dimensionality of the policy's action space."""
        unnorm_key = self._check_unnorm_key(self.norm_stats, unnorm_key)
        return len(self.norm_stats[unnorm_key]["action"]["q01"])

    def get_action_stats(self, unnorm_key: Optional[str] = None) -> Dict[str, Any]:
        """Get all the logged statistics for the given dataset."""
        unnorm_key = self._check_unnorm_key(self.norm_stats, unnorm_key)
        return self.norm_stats[unnorm_key]["action"]
