# P13 환경 설치 가이드 (Windows + RTX 4090)

> 무거운 설치라 단계별로. "P13 환경 설치해줘" 하면 자동으로 진행해줄게요.

## 1. CARLA 시뮬레이터 (~20GB)
1. [CARLA 릴리스](https://github.com/carla-simulator/carla/releases)에서 **Windows 패키지**(예: `CARLA_0.9.15.zip`) 다운로드
2. 압축 해제 (예: `C:\CARLA_0.9.15`) → `CarlaUE4.exe` 실행되면 OK
3. Python API 설치 (CARLA 버전과 파이썬 버전 맞춰야 함):
   ```powershell
   python -m pip install carla==0.9.15
   ```
   > ⚠️ CARLA는 특정 Python(주로 3.7~3.10)만 지원. 현재 3.10이면 대체로 OK.

## 2. PyTorch (CUDA, RTX 4090)
```powershell
python -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
```
확인:
```powershell
python -c "import torch; print(torch.__version__, torch.cuda.is_available(), torch.cuda.get_device_name(0))"
# 기대: 2.x True NVIDIA GeForce RTX 4090
```

## 3. 트랙별 추가 패키지
```powershell
# A, C 공통
python -m pip install numpy opencv-python

# D (VLA) — 4-bit 양자화 + LoRA
python -m pip install transformers accelerate bitsandbytes peft
```

## 4. 동작 확인
1. 터미널1: `CarlaUE4.exe -quality-level=Epic` (4090이니 Epic 화질)
2. 터미널2: `python A_conditional_imitation/collect_data.py --test` (연결 테스트)

## 트러블슈팅
- `carla` pip 설치 실패 → CARLA 패키지 안 `PythonAPI/carla/dist/*.whl` 직접 설치
- CUDA False → 최신 NVIDIA 드라이버 재설치
- VRAM 부족(D) → 4-bit 로드(`load_in_4bit=True`) + LoRA + 배치/해상도 축소
