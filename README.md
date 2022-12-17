
![mcla](https://user-images.githubusercontent.com/18550082/207752764-335a691e-7a15-44f6-bde8-07512bedef7b.png)

## 🥚 메추리알(메뉴 추천 리스트 알고리즘)

- 하루하루 세 번 이상 메뉴를 골라야 하는 우리들. 매번 겪는 검색의 고통을 좀 덜 수는 없을까?!
메뉴뿐만 아니라 함께 식사하는 사람들 등 고려해야 할 점이 많다.
직관적이고 쉽게 메뉴를 골라보자!

</br>
</br>

## 😎 Introduction

- 주제: 메뉴 추천을 받고 내 위치 근처의 식당을 찾을 수 있는 서비스
- 기간: 2022.12.01 ~ 2022.12.15(1차)
- Team: Code 200 하경수([Github](https://github.com/WR-10)), 김민규([Github](https://github.com/kmg0485)), 김재원([Github](https://github.com/ja2w0nii)), 윤장미([Github](https://github.com/R5Z)), 이태은([Github](https://github.com/Taeeun99)), 조인걸([Github](https://github.com/Choding91))
- FE Repo: [https://github.com/A7-TC2-TeamCode200/MRLA_Front.git](https://github.com/A7-TC2-TeamCode200/MRLA_Front.git)
- BE Repo: [https://github.com/A7-TC2-TeamCode200/MRLA.git](https://github.com/A7-TC2-TeamCode200/MRLA.git)
- 시연 영상:

</br>

## 📚 Project Structure

(기술 스택 포함 추후 삽입)

</br>

## 🤝 Project Rules


### API

![screencapture-notion-so-API-f959dc1f0f2c476ea42fe257486ce876-2022-12-15-10_45_34](https://user-images.githubusercontent.com/18550082/207753257-9d8e0ddc-8a24-4b68-960e-d7f5243c4956.png)

</br>

### Figma Mock-up & DB

<img width="976" src="https://user-images.githubusercontent.com/18550082/207754411-6524e5f6-29ee-492b-82ea-6886bac46a65.png">

</br>

<img width="1166" src="https://user-images.githubusercontent.com/18550082/207754251-cb78fe22-63e8-4a59-ae51-ddd027176fd0.png">

</br>


## 📂 Structure

```
┌─MRLA
├── MRLA                            // project
│   ├── urls.py                     // base url
│   ├── settings.py                 // setting
│   └── ...
├── foods                           // app
│   ├── models.py                   // DB Model - Food, FoodComment, Category
│   ├── views.py                    // View Functions
│   ├── serializers.py              // Serializers
│   ├── urls.py                     // food(menu) url
│   ├── collaborative_filtering.py  // AI cosine similarity 
│   ├── fixture.json                // Data.json
│   ├── foods.csv                   // Data.csv
│   ├── likes.csv                   // filtering
│   ├── loader.py                   // csv to json
│   └── ...
├── posts                           // app
│   ├── models.py                   // DB Model - Service, Community, Comment
│   ├── views.py                    // View Functions
│   ├── serializers.py              // Serializers
│   ├── urls.py                     // url
│   └── ...
├── user                            // app
│   ├── models.py                   // DB Model - User
│   ├── views.py                    // View Functions
│   ├── serializers.py              // Serializers
│   ├── urls.py                     // user url
│   └── ...
├── **manage.py**                   // 메인
└── requirements.txt
```
</br>


## 💻 Development


### 로그인/회원가입

- JWT 를 사용한 vaildation 로그인
- (구현중) 소셜 로그인(카카오톡, 구글)

</br>

### 메뉴 추천 시스템 기능

- 사용자 간의 선호 메뉴를 통한 유사도(Cosain Similarity)를 이용한 추천 시스템
- 서비스 시작 부분에서 좋아하는 메뉴를 고르면 메인 페이지에서 사용자를 위한 메뉴를 추천
- 메뉴 카테고리를 새로 고르면 새로운 메뉴를 추천!

</br>

### 추천된 메뉴 상세 페이지

- 메뉴 상세 조회
- (구현중) 메뉴 좋아요 기능
- (구현중) 메뉴에 따른 댓글 CRUD

</br>

### 근처 맛집 확인

- 지도에서 사용자 위치를 확인하여 근처 음식점과 카페 위치를 확인
- 카카오 지도 API 활용

</br>

### 누구랑 먹나요?

- 재미로 보는 혼자 혹은 함께 먹을 사람과 상황에 따른 메뉴 추천 페이지

</br>

### 커뮤니티 게시판

- 메뉴나 맛집에 대한 커뮤니티
- 게시글 목록 조회
- 게시글 작성(Image Preview)
- 커뮤니티 내 게시글 검색 기능

</br>

### 고객센터 게시판

- 서비스 사용 시 문의 내용을 남길 수 있는 게시판 기능
- 사용자는 본인이 작성한 글만 상세 조회 가능
- 어드민(운영자) 계정 확인 후 게시글 상세 조회 / 삭제 가능

</br>

### 프로필 페이지

- 사용자 정보 조회
- 내 프로필 정보 조회 / 수정 / 탈퇴 가능
- 사용자가 좋아요한 메뉴 모아보기
- 사용자가 쓴 커뮤니티 게시글 모아보기

</br>


## 🌠 Service View

(추후 삽입)

</br>

## 🛠 Trouble Shooting

