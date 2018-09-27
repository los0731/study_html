### .name
The name, which uses the `<h2>` tag, should be a little below the image and the text should be bolded, as it is the most important information on the business card. Also we will choose `Green 500` from [Google colors][1] for the tag.

* The top margin of `h2` is `8px`.
* The font-weight is `900`
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

* There are no bullet points on the list.
* The margin for top/right/down/left is `16px 0 0 0`.
* Padding is `0`.
* The size of the text is `16px`
* The line height is `24px`.
* The text color is `#455A64`.


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

