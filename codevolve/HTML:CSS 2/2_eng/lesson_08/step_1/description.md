# Before starting 
let's look at the Google icon!

The are various ways to show image icons in a browser. You can use jpg, png  for image files or svg icon, icon font. Here, the representative way to use the icon font is to use Google material icons. For the Google search page we'll be making, we will use the microphone icon for the voice search and an apps icon. 

For more information about how to better use icon font, check out [Material Design - Icon][2]. For this lesson, all is already pre-set for us to use icon font. let's look at the minimal guidelines for using Google's material icons. 

A line of code is attached to the `<head>` to enable using material icons. Whenever you add this code, you can use material icons. 

```html
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
```

You can also write the code in `<body>`, so that you can use the material icons there too. 

```html
<body>
  <i class="material-icons">mic</i>
  <i class="material-icons">accessibility</i>
  <i class="material-icons">assessment</i>
  <i class="material-icons">alarm</i>    
</body>
```



For more information, see the [Material Icons Guide][3].

Back to Catalog And Start **NEXT STEP**!

[2]:https://material.io/tools/icons
[3]:https://google.github.io/material-design-icons/