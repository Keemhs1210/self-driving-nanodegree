# ───────────────────────────────────────────────────────────────────────────
# P13-D 실습본 — 실제 OpenVLA 코드 기반 (중요 포인트만 비움)
#
# 원본: reference/papers/D_openvla/prismatic/extern/hf/modeling_prismatic.py
#         class OpenVLAForActionPrediction.predict_action()  (lines 506~536)
#       (Kim et al., OpenVLA, arXiv:2406.09246)
#
# ★VLA 핵심 아이디어★: '행동(action)'을 언어 토큰으로 취급한다.
#   VLM이 토큰을 생성 → 그 토큰ID를 역양자화(bin) → [-1,1] 정규화행동 →
#   데이터셋 통계(q01/q99)로 실제 행동 범위로 역정규화.
#
# 비운 곳:
#   STEP 1) 생성된 토큰ID → 이산 bin → bin center(정규화 행동)  [역토큰화]
#   STEP 2) 정규화 행동 → 실제 행동 [역정규화]
# 나머지(generate 호출, 통계 헬퍼)는 원본 그대로.
# 비교: 채운 뒤 원본 modeling_prismatic.py 와 diff.
# ───────────────────────────────────────────────────────────────────────────
from typing import Optional, Dict, Any
import numpy as np
import torch

from prismatic.extern.hf.modeling_prismatic import PrismaticForConditionalGeneration
from prismatic.extern.hf.configuration_prismatic import OpenVLAConfig


class OpenVLAForActionPrediction(PrismaticForConditionalGeneration):
    config_class = OpenVLAConfig

    def __init__(self, config: OpenVLAConfig) -> None:
        super().__init__(config)
        self.norm_stats = config.norm_stats
        # (제공) 행동 이산화 bin: [-1,1] 을 n_action_bins 칸으로
        self.bins = np.linspace(-1, 1, config.n_action_bins)
        self.bin_centers = (self.bins[:-1] + self.bins[1:]) / 2.0
        self.vocab_size = self.config.text_config.vocab_size - self.config.pad_to_multiple_of

    def predict_action(self, input_ids: Optional[torch.LongTensor] = None,
                       unnorm_key: Optional[str] = None, **kwargs) -> np.ndarray:
        """이미지+지시 프롬프트(input_ids) → 연속 행동(np.ndarray)."""
        # (제공) 학습시 형식 맞추기 위한 특수토큰 보정
        if not torch.all(input_ids[:, -1] == 29871):
            input_ids = torch.cat(
                (input_ids, torch.unsqueeze(torch.Tensor([29871]).long(), dim=0).to(input_ids.device)), dim=1)

        # (제공) VLA 추론: 행동 차원 수만큼 토큰 생성
        generated_ids = self.generate(input_ids, max_new_tokens=self.get_action_dim(unnorm_key), **kwargs)

        # ── STEP 1. 역토큰화: 토큰ID → 정규화 행동 ──
        # [할 일]
        #   predicted_action_token_ids = generated_ids[0, -self.get_action_dim(unnorm_key):].cpu().numpy()
        #   discretized = self.vocab_size - predicted_action_token_ids      # 토큰ID를 bin 인덱스로
        #   discretized = np.clip(discretized - 1, 0, self.bin_centers.shape[0]-1)
        #   normalized_actions = self.bin_centers[discretized]              # bin 중심값(=[-1,1] 행동)
        # TODO STEP 1
        raise NotImplementedError("STEP 1: 토큰ID → 정규화 행동 (역양자화)")

        # ── STEP 2. 역정규화: [-1,1] → 실제 행동 ──
        # [할 일]
        #   stats = self.get_action_stats(unnorm_key)
        #   mask = stats.get("mask", np.ones_like(stats["q01"], dtype=bool))
        #   high, low = np.array(stats["q99"]), np.array(stats["q01"])
        #   actions = np.where(mask, 0.5*(normalized_actions+1)*(high-low)+low, normalized_actions)
        #   return actions
        # TODO STEP 2
        raise NotImplementedError("STEP 2: 정규화 행동 → 실제 행동 (역정규화)")

    # ── (제공) 데이터셋 통계 헬퍼 — 원본 그대로 ──
    @staticmethod
    def _check_unnorm_key(norm_stats, unnorm_key):
        if unnorm_key is None:
            assert len(norm_stats) == 1
            unnorm_key = next(iter(norm_stats.keys()))
        assert unnorm_key in norm_stats
        return unnorm_key

    def get_action_dim(self, unnorm_key=None):
        return len(self.norm_stats[self._check_unnorm_key(self.norm_stats, unnorm_key)]["action"]["q01"])

    def get_action_stats(self, unnorm_key=None):
        return self.norm_stats[self._check_unnorm_key(self.norm_stats, unnorm_key)]["action"]
