### <td>
let's organize the `td` style, which is commonly used for body contents of the receipt.
* The `.table-receipt td`'s padding is `24px` for top/down and `16px` for left/right.
* There is a border line at the bottom. The border's width/style/color are set as `2px solid #ECEFF1`.

**Instructions**
1. Apply style to `.table-receipt td`.
    ```css
    .table-receipt td {
    	padding: 24px 16px;
    	border-bottom: 2px solid #ECEFF1;
    }
    ```



### .t-label

let's now define the style of the label. 
* The font size of `.table-receipt .t-label` is `16px`.
* The letter thickness, font-weight, is `700`. 
* The font color is `#78909C`. The color is [Google color][999]'s `Blue grey 400`.

**Instructions**
1. Apply style to `.table-receipt .t-label`.
    ```css
    .table-receipt .t-label {
    	font-size: 16px;
    	font-weight: 700;
    	color: #78909C;
    }
    ```



### .t-price

The price is the most important part of the receipt. let's go ahead and define it's style. 
* `.table-receipt .t-price`'s text size is `24px`.
* The letters are centered.

**Instructions**
1. Apply style to `.table-receipt .t-label`.
    ```css
    .table-receipt .t-price {
    	font-size: 24px;
    	text-align: right;
    }
    ```


​    
### .t-footer

Last but not least, is the style of the footer. 
* `.table-receipt .t-footer`'s padding is `24px`.
* The border at the bottom is `0`.
* The font size is `16px`.
* The font color is `#2196F3`. (same as background color.)
* The font-weight is `700`.
* The letters are centered.

**Instructions**
1. Apply style to `.table-receipt .t-footer`.
    ```css
    .table-receipt .t-footer {
    	padding: 24px;
    	border-bottom: 0;
    	font-size: 16px;
    	color: #2196F3;
    	font-weight: 700;
    	text-align: center;
    }
    ```



Click the **NEXT STEP** button. 

[999]: https://material.io/design/color/#color-usage-palettes