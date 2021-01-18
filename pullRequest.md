## 📢  Pull Request 규칙

### 1. PR용 branch 생성

`$ git checkout -b branch명`

### 2. 소스코드 추가 및 커밋 작성

`$ git add .`

`$ git commit -m "문제 이름"`

### 3. branch에 Push (‼️주의‼️ main에 push하지 말 것)

`$ git push origin branch 명`

### 4. github 사이트에서 Compare & Pull Request 버튼 클릭

1. **Compare & Pull request** 
 
![image](https://user-images.githubusercontent.com/42290273/104888154-b07c0a00-59af-11eb-8715-e6a44bbef1cc.png)


**2. Create pull Request** 

![image](https://user-images.githubusercontent.com/42290273/104888170-b7a31800-59af-11eb-801c-a0bd8c4fb389.png)


### 5. PR 승인 및 merge 후 branch 삭제

- 다른 브랜치에서 해당 명령어 실행

`$ git branch -d branch명` ( **local** 브랜치 삭제 )

`$ git push origin --delete branch명)` ( **remote** 브랜치 삭제 )

☑️ **branch 확인 방법**

- local branch 확인 :  `$ git branch`
- remote branch 확인 :  `$ git branch -r`



