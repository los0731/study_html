### .card-type, .card-tag
let's style the type and tag text, located on the left of the card. `.card-type` and `.card-tag` have to be defined simultaneously. When selecting more than 2 classes at the same time, use `, ` between them. 

* The margin of `.card-type, .card-tag` is `16px 0 0 0` for top/right/down/left.
* The font size is `12px`.
* The font-weight is `400`.
* The font color is `#90949C`.


**Instructions**
1. Apply style to `.card-type,` and `.card-tag`.
    ```css
    .card-type, 
    .card-tag {
      margin: 16px 0 0 0;
      font-size: 12px;
      font-weight: 400;
      color: #90949C;
    }
    ```



### Hover style
Usually only `VIDEO(`.card-type`)` can be seen and  `VIEW MORE(`.card-tag`)` cannot. When we hover the mouse over the card, `VIDEO` should disappear and `VIEW MORE` should pop up. 

1. There are `VIDEO` and `VIEW MORE`. 
2. `VIEW MORE` cannot be seen. 
3. When the mouse is hovered over the card, `VIDEO` disappears. 
4. When the mouse is hovered over the card, `VIEW MORE` appears. 

let's use CSS for 1, 2, 3. 


**Instructions**
1. Don't show `.card-tag`

    ```css
    .card-tag {display: none;}
    ```

2. Don't show `.card-type` that is in `.card:hover`.

    ```css
    .card:hover .card-type {display: none;}
    ```

3. Show `.card-tag` that is in `.card:hover`.

    ```css
    .card:hover .card-tag {display: block;}
    ```


Click the **NEXT STEP** button.



## TIPS!

- The selector is kind of slow. What should I do if I want to apply a style to two classes at the same time? 

  > Let me introduce you to a few popular selectors. 
  >
  > * Apply to A and B simultaneously 
  >
  >   ```css
  >   .classA, .classB {...} /* Between the classes use ',' to seperate them. */
  >   
  >   /* or */
  >   
  >   .classA, 
  >   .classB {...} /* For better readability, you can also use wrapping for the classes.  */
  >   
  >   ```
  >
  > * All the B in the A
  >
  >   ```css
  >   .classA .classB {...} /* Skip only one line.  */
  >   ```
  >
  > * B in the very first phase of A
  >
  >   ```css
  >   .classA > .classB {...} /* Put '>' mark between classes.  */
  >   ```
