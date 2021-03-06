# M-Language
**마빅 헌정 프로그래밍 언어, 『M』**

M은 2019년부터 이어져 오고 있는 햇수로 4년째의 오래된 역사를 가진, 그러나 존폐 위기에 처한
**마[검열됨]** 를 보존하기 위해 제작될 예정입니다.

## 문법
### M에서 사용되는 키워드

```
- . / , / ? / ! / ㅋ

- 마
- 빅
- 엉
- 뽈
- 롱
- 훌륭
- 무빙
- 이민수
- 고소

- 마임 엉덩이 뽈록
- 마이 엉덩이는 뽈록이냐 ㄹㅇ
```

### Main 함수와 End
모든 코드는 『마임 엉덩이 뽈록』으로 시작해 『마이 엉덩이는 뽈록이냐 ㄹㅇ』으로 끝납니다.
그 전 후의 키워드는 모두 주석으로써 무시됩니다.

### 정수: . / ,

```
. => +1
, => -1
```

모든 정수형 (변수 포함) 을
붙여서 쓰는 경우 => 덧셈 연산자

한 칸 띄어쓰기 하는 경우 => 곱셈 연산자
입니다.

### 뽈 / 롱
변수의 위치를 나타냅니다.

```
롱 => 0번째 변수
뽈롱 => 1번째 변수
뽀올롱 => 2번째 변수
뽀오올롱 => 3번째 변수
뽀오오올롱 => 4번째 변수

...

뽀 + 오 * n + 올롱 => n + 3번째 변수
```

첫 인덱스 3개만 예외입니다; 『뽈, 뽈롱, 뽀올롱』

### 마
뒤에 따라오는 변수의 위치와 값으로 변수를 선언합니다.

```
마뽀올롱..
// 2번째 변수에 정수 2를 대입합니다.
```

### 빅
변수를 호출합니다

```
빅 => 0번째 변수
비익 => 1번째 변수
비이익 => 2번째 변수
```

### 엉
콘솔 in / out put을 관리합니다

#### 엉?
콘솔에서 입력을 받습니다. 자동으로 정수형 변환이 됩니다.

```
마뽀올롱엉? => 2번째 변수에 콘솔 입력을 저장합니다.

...

마뽀올롱,,엉? => 2번째 변수에 콘솔 입력에서 2를 뺀 값을 저장합니다.
// 변수와 정수를 혼합해서 쓸 때에는, 정수를 먼저 쓰는 것이 규칙입니다.
```

#### 엉!
콘솔에 출력합니다.

```
엉!비익 => 1번째 변수를 출력합니다.
```

### 무빙
따라오는 위치의 정수 줄로 이동합니다.

```
무빙... .. => 6번째 줄로 이동
```

자연수 형태가 따라와야 합니다.

### 이민수
전지전능하신 이 시대의 현자, 『이 민수』옹 께서 변수의 진위 여부를 판단해 주십니다.

```
이민수{변수|정수}ㅋ{부탁드릴 소원}
```

따라오는 변수가 마빅의 잔고만하다면 소원 성취를 해 주십니다.

```
마뽈롱 => 1번째 변수에 0 대입
이민수뽈롱ㅋ고소,,, => 만약 뽈롱 == 0 이라면 -3을 출력하고 강제종료.
```

### 훌륭
훌륭한 마빅의 대 기술로 정수에 대응하는 유니코드를 출력합니다.

```
훌륭...... => 유니코드 006 문자를 콘솔에 출력합니다.

// 응용
훌륭엉?비이익... => 사용자 입력에 2번째 변수를 더한 것에 3을 더한 값에 대응하는 유니코드 문자를 콘솔에 출력합니다.
```

### 고소
빡친 마빅을 호출하여, 따라오는 정수를 출력하고 프로그램을 빡종시킵니다.

```
고소,,, => 콘솔에 -3 출력, 프로그램 종료
고소비이익 => 콘솔에 2번째 변수 출력, 프로그램 종료
```

그러나 자비로운 마빅은 『이민수』에게 자비를 베풉니다.
변수 호출이나 정수를 출력하지 않고 키워드 "이민수" 를 쓰면
정수 "150000" 을 출력하고 프로그램은 강제종료 되지 않습니다.

```
고소이민수 => 콘솔에 150000 출력
```

## 예제

### 두 정수를 입력받아 덧셈, 곱셈 결과를 출력.

```
마임 엉덩이 뽈록

마뽈롱엉?
마뽀올롱엉?

마뽀오올롱비익 비이익
마뽀오오올롱비익비이익

엉!비이이익
고소비이이이익

마이 엉덩이는 뽈록이냐 ㄹㅇ
```

### 입력
```
5
7
```
### 출력
```
35
12
```
