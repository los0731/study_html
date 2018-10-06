## 결론

하나의 프로퍼티당 하나의 CHECKS를 사용해야함. 

```css
.form-search:hover,
.form-search:focus {
  max-width: 630px;
}
```

위 css 코드에 대한 정규표현식은 다음과 같다.

```python
\.form-search:hover,\s*\.form-search:focus\s*{[\s|\S]*?max-width:\s*630px;[\s|\S]*?}
```

다음의 템플릿을 수정하면 편하다.

```python
\.class-name\s*\s*{\s*
  [\s|\S]*?
    padding:\s*16px\s*16px\s*;\s*
  [\s|\S]*?
}

\.class-name\s*\s*{\s*[\s|\S]*?padding:\s*16px\s*16px\s*;\s*[\s|\S]*?}

```





## 설명

`\s`: Matches any space, tab or newline character. 공백 문자를 찾음. 띄어쓰기, 줄바꿈, 탭 모두.
`\S`: Matches anything other than a space, tab or newline.
`*`: Matches as many characters as possible. 없구나 무한대로 있거나 모두 찾음
`[\s|\S]`: 모든 문자



https://regexr.com/40oqm

```
[\s|\S]*?max-width:\s*630px;[\s|\S]*?}


\.form-search:hover,\s*\.form-search:focus\s*{[\s|\S]*?max-width:\s*630px;[\s|\S]*?}
\.form-search:hover,\s*\.form-search:focus\s*{[\s|\S]*?width:\s*630px;[\s|\S]*?}
\.form-search:hover,\s*\.form-search:focus\s*{[\s|\S]*?width:\s*630px;[\s|\S]*?}
```





## 조건

1. 선택자는 이름은 딱 맞게 작성해야함.
2. 프로퍼티의 순서는 바뀌어도 됨
3. 프로퍼티의 값은 딱 맞게 작성해야함. 

다음을 만족하는 정규표현식을 작성하시오

```css
.form-search:hover,
.form-search:focus {
  margin: 0 auto;
  max-width: 630px;
  width: calc(100% - 32px);
  box-shadow: 0 2px 2px 0 rgba(0,0,0,0.16), 0 0 0 1px rgba(0,0,0,0.08);
}

/* 값의 순서는 바뀌어도 됨 */
.form-search:hover,
.form-search:focus {
  box-shadow: 0 2px 2px 0 rgba(0,0,0,0.16), 0 0 0 1px rgba(0,0,0,0.08);
  margin: 0 auto;
  width: calc(100% - 32px);
  max-width: 630px;
}

/*  모든 줄 바꿈은 무시해도됨. */
.form-search:hover, .form-search:focus { margin: 0 auto; max-width: 630px; width: calc(100% - 32px); box-shadow: 0 2px 2px 0 rgba(0,0,0,0.16), 0 0 0 1px rgba(0,0,0,0.08);}

/* 띄어 쓰기 2회 이상은 모두 무시 (1회로 침) */
.form-search:hover,  .form-search:focus    {  margin:   0 auto;     max-width: 630px; width: calc(100% - 32px); box-shadow: 0 2px 2px 0 rgba(0,0,0,0.16), 0 0 0 1px rgba(0,0,0,0.08);}
```



