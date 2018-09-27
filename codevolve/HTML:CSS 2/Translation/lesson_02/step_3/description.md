# CSS
### <body>
Set the color of the card to white and the background to purple.

* The margin of the body is `0`.
* For the padding all is `16px` for top/right/down/left.
* Background color is `#512DA8`.

**Instructions**
1. Apply style to `body`. 
    ```css
    body {
      margin: 0;
      padding: 16px;
      background-color: #512DA8;
    }
    ```



### .birthday-card
`.birthday-card` is the space to write the actual card

* The margin is `40px` for top/down, `auto` for left/right
* Padding is `16px`
* The maximum width is `400px`.
* Background color is `white`.
* The text range is `center`.
* The shadow's x-axis/y-axis/blur/size/color is `0 24px 40px -8px #311B92`.

**Instructions**
1. Apply style to `birthday-card`.
    ```css
    .birthday-card {
      margin: 40px auto;
      padding: 16px;
      max-width: 400px;
      background-color: white;
      text-align: center;
      box-shadow: 0 24px 40px -8px #311B92;
    }
    ```



Click the **NEXT STEP** button.



## TIPS!
* What are the criteria for chosing colors? 
    > If you're not a designer, we recommend using [Google Colors][https://material.io/design/color/#color-usage-palettes]'s pallet of 500 color lines. The 500 color lines are the what can be called the standard flat colors, clear and vivid. As the numbers within the 'lines' go down the colors brighten, as they go up they get darker. 
    > In Google Colors I usually choose one color line (which is called a theme color). The rest of the colors I prefer to choose in unity with the blue grey color. Otherwise, I use only colors that match the message, meaning intended:
    >
    > - For links it's `Blue500`
    > - For negative things like danger, delete, removing, error etc. we use `Red500`
    > - For elements that need users' attention, like warnings, caution signs, we use `Orange500`
    > - For positive messages like upload complete, writing complete, success, correct answer etc. we use `Green500`
* Isn't the shadow's color black?

    > Usually when we apply the shadow's color values, we use black. However, a lot of designers don't use black for the shadow. Shadows usually are close to the color of the background. Therefore when choosing the shadow color, we recommend going for a slightly darker shade than the background. 
    >
    > For example, in the above Google Colors, if we use `Blue grey 50~300` on a white background, the background is defined as `Blue500` and to create a natural looking the shadow we should use `Blue700~900`. In a slightly more specialist approach, transparent values are used. We recommend values based on a white basic background, where something like `rgba(50,50,80,.08)` with slightl transparency, will give natural looking bluish grey color. 
* Don't you notice that the value numbers are multiples of 8?
    > That's right! The following is the reason for using the multiple of 8 for layout, space gaps, size, numerical figures etc.
    > 1. It's easy to estimate and soon will be easy for collaborating on projects. it's because we need not only use values known only to designers, but something that's easy to predict, therefore if there are no designers around, developers can still adjust the values on their own. 
    > 2. That way an efficient layout can be designed, that meets the standards of various devices and displays. 
    > 3. In other words, we can provide a regular and consistent user experience. 
    > 4. Let's look into this a bit more.  - https://builttoadapt.io/intro-to-the-8-point-grid-system-d2573cde8632