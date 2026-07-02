# 이미지 WebP 변환 및 CDN 가이드

이 문서는 `heroes/` 폴더 내의 이미지 파일 형식을 JPG에서 WebP 포맷으로 변환하고 최적화하기 위한 절차를 기록합니다.

## 🛠 사용된 도구
- **Python 3.11+**
- **Pillow (PIL)**: 이미지 파일 포맷 WebP 변환용

## 🚀 이미지 변환 방법
새로운 JPG 이미지를 추가하거나 기존 이미지를 수정한 뒤, 아래 명령어를 실행하면 `heroes/` 폴더 내의 JPG 파일들이 크기와 레이아웃 변경 없이 그대로 WebP 이미지로 일괄 변환되고 기존 JPG 파일들은 삭제됩니다.

```powershell
python process_images.py
```

### 처리 규칙
1. **Format Conversion**: 모든 `.jpg` 파일은 원래의 해상도와 품질을 유지한 채 `.webp` 포맷으로 변환됩니다.
2. **Unicode Normalization**: 파일명에 자모 분리 현상(NFD)이 없도록 완성형(NFC)으로 자동 정규화되어 저장됩니다.

## 🌐 무료 CDN(콘텐츠 전송 네트워크) 활용 가이드
깃허브 리포지토리에 저장된 이미지를 외부 서비스에서 불러와 사용할 때는 깃허브 raw 링크 대신 무료 CDN을 이용하면 로딩 속도가 비약적으로 향상되며 레이트 리밋 우려가 없습니다.

- **기존 raw 주소**: `https://raw.githubusercontent.com/유저명/리포명/main/heroes/hero1.webp`
- **statically.io 적용 주소**: `https://cdn.statically.io/gh/유저명/리포명/main/heroes/hero1.webp`
- **jsDelivr 적용 주소**: `https://cdn.jsdelivr.net/gh/유저명/리포명@main/heroes/hero1.webp`

## 📝 작업 히스토리
- **2026-07-02**: 기존 JPG 파일들을 단순 WebP로 일괄 변환 완료. 자모 분리 이름 정규화 적용 및 기존 JPG 삭제 완료.

