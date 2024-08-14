# **OpenCV를 이용한 탁구 자동 스코어링 제품**

## **프로젝트 개요**

이 프로젝트는 탁구 경기를 자동으로 스코어링하는 소프트웨어 및 하드웨어 시스템을 개발하는 것을 목표로 합니다. OpenCV를 활용하여 이미지 처리를 통해 탁구 공을 실시간으로 추적하고 점수를 자동으로 기록합니다.

## **기술 스택**

- **소프트웨어 개발 환경:**
  - Google Colab
  - Jupyter Notebook
  - Pycharm
  - VS Code
  - Nomachine

- **개발 언어:**
  - Python
  - Arduino

- **사용 라이브러리:**
  - OpenCV
  - Python Numpy

- **임베디드 시스템 개발 환경:**
  - Python
  - OpenCV.net
  - PowerShell

- **하드웨어 개발 환경:**
  - Raspberry Pi 4
  - Webcam
  - 4-Digital tube LED Display

## **주요 기능**

- **이미지 분할 및 공 추적:** OpenCV를 사용하여 공의 위치를 실시간으로 추적하고 경계 영역을 식별합니다.
- **스코어링 알고리즘:** 자동으로 점수를 기록하고, 4-Digital tube LED Display를 통해 점수를 표시합니다.
- **하드웨어 통합:** Raspberry Pi 4와 Webcam을 활용하여 실시간 데이터를 처리하고 결과를 디스플레이합니다.

## **설치 및 실행**

1. **필요한 라이브러리 설치:**

   ```bash
   pip install opencv-python numpy
   ```

2. **하드웨어 준비:**
   - Raspberry Pi 4에 Webcam과 4-Digital tube LED Display를 연결합니다.

3. **코드 실행:**

   - **소프트웨어 실행:**

     ```bash
     python main.py
     ```

   - **Arduino 스케치 업로드:**
     - Arduino IDE에서 `arduino_code.ino` 스케치를 업로드합니다.

## **사용 방법**

1. **비디오 스트리밍:** 카메라를 통해 비디오 스트리밍을 시작합니다.
2. **점수 기록:** 공의 위치를 추적하고 점수를 자동으로 기록합니다.
3. **점수 표시:** 점수가 4-Digital tube LED Display에 표시됩니다.

## **참고 자료**

- [Ball Tracking with OpenCV](https://pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/)
- [Table Tennis Computer Vision](https://github.com/vmarquet/table-tennis-computer-vision)

## **프로젝트 구조**

- `main.py`: 메인 프로그램 스크립트
- `arduino_code.ino`: Arduino 스케치
- `docs/`: 프로젝트 문서 및 흐름도
- `hardware/`: 하드웨어 관련 설정 및 설명

## **기여**

이 프로젝트는 저와 연구실 석사 형님과 협력하여 개발되었습니다.

## **라이센스**

이 프로젝트는 [MIT 라이센스](LICENSE)에 따라 라이센스가 아직 신청하지 않아서 부여가 안 됩니다.

## **연락처**

- **이메일:** myfuzei@gmail.com
- **GitHub:** [https://github.com/gebalja-Tommy](https://github.com/gebalja-Tommy)

---
