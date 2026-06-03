"""
P13-D: VLA 추론 주행 (직접 채우는 스켈레톤)
사전학습 VLM(예: Qwen2-VL / LLaVA)을 4-bit 로 로드해
카메라 이미지 + 언어 규칙 → 구조화된 행동(JSON) → CARLA 제어.
설명: README.md  /  설치: ../SETUP.md (transformers, bitsandbytes, accelerate, peft)
"""
import json
import torch
from PIL import Image
# from transformers import AutoModelForVision2Seq, AutoProcessor, BitsAndBytesConfig

MODEL_ID = "Qwen/Qwen2-VL-7B-Instruct"   # 원하는 VLM 으로 교체 가능

SYSTEM_PROMPT = """너는 자율주행 에이전트다. 전방 카메라 이미지를 보고 운전 규칙을 지켜 행동을 결정한다.
규칙: 빨간불/정지선이면 정지. 앞차가 느리고 옆차선이 비면 추월. 보행자 있으면 감속.
반드시 아래 JSON 형식으로만 답하라:
{"reason": "<한 줄 근거>", "action": "<GO|STOP|LEFT|RIGHT>", "throttle": 0~1, "brake": 0~1, "steer": -1~1}"""


def load_model():
    # [STEP 1] 4-bit 양자화로 VLM + 프로세서 로드
    #   bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16)
    #   model = AutoModelForVision2Seq.from_pretrained(MODEL_ID, quantization_config=bnb,
    #                                                  device_map="auto")
    #   processor = AutoProcessor.from_pretrained(MODEL_ID)
    #   return model, processor
    raise NotImplementedError("STEP 1: VLM 4-bit 로드")


def decide(model, processor, image: Image.Image, instruction: str) -> dict:
    """이미지 + 지시 → 행동 dict."""
    # [STEP 2] 메시지 구성 (system + 이미지 + 사용자 지시) → processor 로 입력 텐서화
    # [STEP 2] model.generate(...) 로 텍스트 생성
    # [STEP 3] 생성 텍스트에서 JSON 부분만 추출해 json.loads → dict 반환
    #   (파싱 실패 시 안전 기본값 {"action":"STOP", "throttle":0,"brake":1,"steer":0})
    # TODO STEP 2~3
    raise NotImplementedError("STEP 2~3: 추론 + 파싱")


def to_carla_control(decision: dict):
    """행동 dict → carla.VehicleControl. (CARLA 연결부는 A의 drive.py 패턴 재사용)"""
    import carla
    return carla.VehicleControl(
        throttle=float(decision.get('throttle', 0.0)),
        brake=float(decision.get('brake', 0.0)),
        steer=float(decision.get('steer', 0.0)),
    )


if __name__ == '__main__':
    # 오프라인 테스트: 이미지 한 장으로 결정만 찍어보기 (CARLA 없이도 가능)
    model, processor = load_model()
    img = Image.open('sample_front.png')
    print(decide(model, processor, img, "안전하게 직진하되 신호를 지켜라"))
