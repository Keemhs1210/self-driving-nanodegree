# P2 — Traffic Sign Classification (교통표지판 분류 · 인지)

🟦 **인지** | **언어**: Python + TensorFlow/Keras | **난이도**: 입문~중급

## 목표
독일 교통표지판(GTSRB) 43종을 **CNN으로 분류** (검증 정확도 ≥ 0.93 목표).

## 데이터
- German Traffic Sign Dataset (pickle: `train.p`, `valid.p`, `test.p`, 32×32 RGB)
- 다운로드: Udacity 제공 [traffic-signs-data.zip](https://s3-us-west-1.amazonaws.com/udacity-selfdrivingcar/traffic-signs-data.zip) → `data/` 에 압축 해제
- 레퍼런스: `reference/.../project_2_traffic_sign_classifier/Traffic_Sign_Classifier.ipynb`

## 파이프라인
```
1. 데이터 로드 (pickle)        train/valid/test
2. 전처리                      그레이스케일/정규화 (x/127.5 - 1)
3. CNN 모델                    LeNet 변형 (Conv-Pool ×2 → FC ×2 → softmax43)
4. 학습                        Adam, epochs, dropout
5. 평가                        test accuracy, 혼동행렬
```

## 핵심 개념
- **합성곱(Conv)**: 지역 패턴(에지/곡선) 추출, 파라미터 공유.
- **풀링**: 다운샘플, 위치 불변성.
- **Dropout**: 과적합 방지.
- 클래스 불균형 → 데이터 증강(회전/이동/밝기) 고려.

## 환경
> ⚠️ TensorFlow 미설치. 설치: `python -m pip install tensorflow` (Python 3.10 호환).
> 막히면 "P2 환경 세팅해줘".
