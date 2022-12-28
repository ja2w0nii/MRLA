
![mcla](https://user-images.githubusercontent.com/18550082/207752764-335a691e-7a15-44f6-bde8-07512bedef7b.png)

## 🐣 메추리알(메뉴 추천 리스트 알고리즘)

하루하루 세 번 이상 메뉴를 골라야 하는 우리들. 매번 겪는 검색의 고통을 좀 덜 수는 없을까?!</br>
메뉴뿐만 아니라 함께 식사하는 사람들 등 뭘 먹을지 고민하는 데에도 고려할 점이 많죠.</br>
서비스 메추리알은 직관적이고 쉽게 메뉴를 고를 수 있게 도와드립니다!</br>
 - 한식, 양식, 아시안... 등 카테고리에 맞춰 메뉴를 추천해드려요.
 - 추천받은 메뉴를 파는 근처 식당을 바로바로 찾아볼 수 있어요.
 - 카테고리에 맞는 음식점의 위치를 바로 확인할 수 있어요. (+카페도 볼 수 있어요!)
 - 커뮤니티에서 먹고 싶은 음식이나 맛집에 대한 정보를 나눌 수 있어요.
 - 맛집을 많이 아는 유저를 발견했나요? 팔로우하고 정보를 교환해요.
 
 #### 바로가기 👉 https://mechurial.mrla.tk/

</br>

## 😎 Introduction

- 주제: 메뉴 추천을 받고 내 위치 근처의 식당을 찾을 수 있는 서비스
- 기간: 2022.12.01 ~ 2022.12.28
- Team: Code 200 하경수([Github](https://github.com/WR-10)), 김민규([Github](https://github.com/kmg0485)), 김재원([Github](https://github.com/ja2w0nii)), 윤장미([Github](https://github.com/R5Z)), 이태은([Github](https://github.com/Taeeun99)), 조인걸([Github](https://github.com/Choding91))
- FE Repo: [https://github.com/A7-TC2-TeamCode200/MRLA_Front.git](https://github.com/A7-TC2-TeamCode200/MRLA_Front.git)
- BE Repo: [https://github.com/A7-TC2-TeamCode200/MRLA.git](https://github.com/A7-TC2-TeamCode200/MRLA.git)
- 시연 영상: https://youtu.be/d7c8cj_qlmo

</br>

## 📚 Project Structure
### STACKS
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/Djangorestframework-092E20?style=for-the-badge&logo=Django&logoColor=white"> <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=for-the-badge&logo=Javascript&logoColor=white"> <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white"> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white">

</br>

<img width="637" alt="스크린샷 2022-12-28 오후 8 32 25" src="https://user-images.githubusercontent.com/18550082/209807208-de18c115-a730-4597-ad19-74d38c0dd8ff.png">

</br>

## 🤝 Project Rules


### API [https://patch-powder-891.notion.site/API-f959dc1f0f2c476ea42fe257486ce876](https://www.notion.so/399c7172b86d4fb98c69217d1914ab98?v=4aae1c0655e54e1e9b8278d5a20bc819)

</br>

### Figma Mock-up & DB

<img width="976" src="https://user-images.githubusercontent.com/18550082/209805563-c600cd2b-6959-4928-99c7-424b97fe6558.png">

</br>

<img width="1166" src="https://user-images.githubusercontent.com/18550082/209805067-559c682e-4c59-4381-8342-5a92af1d14f0.png">

</br>


## 📂 Structure

```
┌─MRLA
├── MRLA                            // project
│   ├── settings.py                 // setting
│   ├── urls.py                     // base url
│   └── ...
├── foods                           // app
│   ├── collaborative_filtering.py  // AI cosine similarity 
│   ├── fixture.json                // Data.json
│   ├── foods.csv                   // Data.csv
│   ├── likes.csv                   // filtering
│   ├── loader.py                   // csv to json
│   ├── models.py                   // DB Model - Food, FoodComment, Category
│   ├── serializers.py              // Serializers
│   ├── urls.py                     // food(menu) url
│   ├── views.py                    // View Functions
│   └── ...
├── posts                           // app
│   ├── models.py                   // DB Model - Service, Community, Comment
│   ├── serializers.py              // Serializers
│   ├── urls.py                     // url
│   ├── views.py                    // View Functions
│   └── ...
├── users                           // app
│   ├── models.py                   // DB Model - User
│   ├── serializers.py              // Serializers
│   ├── urls.py                     // user url
│   ├── views.py                    // View Functions
│   └── ...
├── **manage.py**                   // 메인
└── requirements.txt
```
</br>


## 💻 Development


### 로그인/회원가입

- JWT 를 사용한 vaildation 로그인
- 소셜 로그인(카카오톡)

</br>

### 메뉴 추천 시스템 기능

- 선호 메뉴를 통한 유사도(Cosine Similarity)를 이용한 추천 시스템
- 카테고리 별로 새로운 메뉴를 추천
- 네비바 상단에서 메뉴 검색 가능

</br>

### 추천된 메뉴 상세 페이지

- 메뉴 상세 조회
- 메뉴 좋아요 기능
- 메뉴에 따른 댓글 CRUD
- 해당 메뉴를 파는 근처 식당 확인 기능

</br>

### 근처 맛집 확인

- 카카오 지도 API 활용 
- 지도에서 사용자 위치를 확인하여 카테고리 별 근처 식당과 카페의 위치 확인

</br>

### 누구랑 먹나요?

- 재미로 보는 혼자 혹은 함께 먹을 사람과 상황에 따른 메뉴 추천 페이지

</br>

### 커뮤니티 게시판

- 메뉴나 맛집에 대한 커뮤니티
- 게시글 목록 조회
- 게시글 작성(Image Preview 기능 포함)
- 게시글 좋아요와 댓글 기능
- 커뮤니티 내 게시글 검색 기능
- 글을 작성한 사용자의 프로필 확인 가능

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
- 사용자가 좋아요한 게시글 모아보기
- 팔로잉과 팔로워 확인 가능
- 다른 사용자 프로필에서 팔로우/언팔로우 가능

</br>

### 사용자 팔로잉

- 게시글이나 댓글을 작성한 사용자의 프로필을 확인하여 팔로우/언팔로우 가능

</br>

## 🌠 Service View

<details>
<summary>회원가입, 로그인</summary>
<div markdown="1">
<img width="364" src="https://user-images.githubusercontent.com/18550082/209781029-021ac793-bdaf-46ec-93e8-51d6865d569c.png"> <img width="364" src="https://user-images.githubusercontent.com/18550082/209781078-26301ef0-b0a8-451f-9120-309c004b7ed7.png">
</div>
</details>

<details>
<summary>메인 페이지 - 메뉴 추천, 메뉴 검색, 프로필 드롭다운</summary>
<div markdown="2">
<img width="364" src="https://user-images.githubusercontent.com/18550082/209782864-2f9491b7-3a1e-401f-8134-feb022a6a53b.png"> <img width="364" src="https://user-images.githubusercontent.com/18550082/209781722-e3c5e076-4737-47e7-9e08-650ea86783c0.png">
</div>
</details>

<details>
<summary>추천 메뉴 상세, 해당 메뉴를 파는 근처 식당 보기(사용자 위치 기반)</summary>
<div markdown="3">
<img width="364" src="https://user-images.githubusercontent.com/18550082/209799654-548294d4-7659-4e3a-97d1-41aeeaa84240.png"> <img width="364" src="https://user-images.githubusercontent.com/18550082/209799666-9a670e8e-f95e-41bc-8639-5ff8d98c310d.png">
</div>
</details>

<details>
<summary>카테고리 별 근처 맛집 보기(사용자 위치 기반), 누구랑 먹나요? 기능</summary>
<div markdown="4">
<img width="364" src="https://user-images.githubusercontent.com/18550082/209800497-45084eef-36fd-44c0-bdcd-06b6eef83b88.png"> <img width="364" src="https://user-images.githubusercontent.com/18550082/209800720-db32bfdc-6fc2-487e-9781-3d9a72ac74c3.png">
</div>
</details>

<details>
<summary>커뮤니티 - 게시글 작성/수정/삭제, 검색 기능</summary>
<div markdown="5">
<img width="364" src="https://user-images.githubusercontent.com/18550082/209802033-6d67b716-ce94-4a8c-a756-cc3ce3b9a3ad.png"> <img width="364" src="https://user-images.githubusercontent.com/18550082/209802095-ab54e1c0-5c49-4b1d-af2d-69b64da89433.png"> <img width="364" src="https://user-images.githubusercontent.com/18550082/209802137-5e851527-dd16-4ebc-b2fd-b0a07294caa6.png">
</div>
</details>

<details>
<summary>고객센터 - 게시글 작성 기능</summary>
<div markdown="6">
<img width="364" src="https://user-images.githubusercontent.com/18550082/209802566-7070e17e-b283-49c1-834c-b169bc808dc7.png"> <img width="364" src="https://user-images.githubusercontent.com/18550082/209802561-90791eda-96fc-47ab-ba0f-296159ee48f8.png">
</div>
</details>

<details>
<summary>마이 프로필 - 좋아요한 메뉴와 게시글/작성한 글 모아보기, 프로필 수정/탈퇴, 사용자 팔로잉</summary>
<div markdown="7">
<img width="364" src="https://user-images.githubusercontent.com/18550082/209803672-2e89ea3a-5de4-4e6e-a612-1c5f7b96f7d9.png"> <img width="364" src="https://user-images.githubusercontent.com/18550082/209803822-a47e5387-5ca7-4549-8295-a275d6c35399.png"> <img width="364" src="https://user-images.githubusercontent.com/18550082/209803902-60896be8-600b-4553-a6b8-b3293013b11c.png"> <img width="364" src="https://user-images.githubusercontent.com/18550082/209803967-042e0b22-b971-47d7-b0d4-4224024585e8.png"> 
</div>
</details>

</br>

## 🛠 Trouble Shooting

