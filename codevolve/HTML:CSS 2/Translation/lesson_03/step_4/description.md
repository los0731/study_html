### .name
The name, which uses the `<h2>` tag, should be a little below the image and the text should be bolded, as it is the most important information on the business card. Also we will choose `Green 500` from [Google colors][1] for the tag.

* `h2`의 위 마진은 `8px`입니다.
* 글씨 두께는 `900`입니다.  
* The font color is `#4CAF50`.

**Instructions**
1. Apply style to `.name`.
    ```css
    .name {
    	margin-top: 8px;
    	font-weight: 900;
    	color: #4CAF50;
    }
    ```



### .information

We used a list tag without any specific order, to write the job position, phone number and email address information. To make it more visually appealing, we should remove the bullet points. Notice that in the list tag there are default options for margin and padding. Therefore we should define the values for both the margin and the padding, to get the desired spacing of the list tag. 

* 리스트의 불렛 마크가 없습니다.
* 마진은 상/우/하/좌 `16px 0 0 0` 입니다.  
* Padding is `0`.
* 글씨 크기는 `16px`입니다.
* 행간은 `24px`입니다.
* 글씨 색상은 `#455A64`입니다.


**Instructions**
1. Apply style to `.information`. 
    ```css
    .information {
        list-style: none;
        margin: 16px 0 0 0;
        padding: 0;
        font-size: 16px;
        line-height: 24px;
        color: #455A64;
    }
    ```



Click the **NEXT STEP** button.



## TIPS! 
* What are the figures for `font-weight`?

    > For the font-weight we can use `light`, `normal`, `bold`, but we can also apply numbers. You can select values from `100` to `900`, where `900` is the thickest aka. Most bold.  


[1]: https://material.io/design/color/#color-usage-palettes

