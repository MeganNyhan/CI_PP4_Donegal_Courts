# Donegal Courts Blog
 
<img src="" alt="Mockup of my blog across multiple devices">
<a href="https://donegalcourts.herokuapp.com/" alt="link to donegal courts blog" target="_blank" rel="noopener">Link to The Donegal Courts Blog</a>

## Project Goals 
<ul>
    <li> The main goal of this project is to create a platform for locals of Donegal to have a place to read and stay informed about the goings on.</li>
    <li>It also aims to create a place for locals to have a public platform (through a comments section) about the stories that have come out of the recent court hearings.</li>
    <li> Finally, the blog will be fully functional from an admin point of view where the admin can manage posts and comments that will be display on the site. They are also responisble for adding content to the site, so any posts that are written need to be editable.</li>
</ul>
<hr>

## Table of Contents
1. [Project Goals](#project-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements](#user-requirements)
    3. [User Stories](#user-stories)
3. [Technical Design](#technical-design)
    1. [Flow Chart](#flow-chart)
    2. [Database Diagram](#database)
    3. [User Manual](#user-manual)
    4. [Wireframes](#wireframes)
4. [Technology](#technology)
    1. [Develpoment Languages Used](#develpoment-languages-used)
    2. [Frameworks and Tools used](#frameworks-and-tools-used)
5. [Features](#features)
6. [Testing](#testing)
    1. [Python Validation](#python-validation)
    2. [HTML Validation](#html-validation)
    3. [CSS Validation](#css-validation)
    4. [JavaScript Validation](#javascript-validation)
    5. [Accessibility] (#accessibility)
    6. [Performance] (#performance)
    7. [Testing user stories](#testing-user-stories)
7. [Bugs](#Bugs)
8. [Deployment](#deployment)
9. [Credits](#credits)
10. [Acknowledgements](#acknowledgements)
11. [Future Features](#future-features)

### User Experience:

### Target Audience 
<p>The Donegal Courts blog was inspired by the local newspaper of Donegal - the Donegal News/ Derry people, so the target audience would be of readers of that or for people who are native to Donegal that live away and want to stay up to date. In short, the Target audience is mainly Donegal Natives or people who have Donegal Ties that want to stay up to date with the court listings. </p>

### User Requirements
<p>As I have mentioned, the blog has a very niche target audience. However, the age demographics are quite broad and because of this the blog has to be easy to use for every age group. I have taken the following approach to make sure that all User Requirements to access and use the blog has been covered:</p>
<ul>
    <li>Have a clear understanding of the layout of the site -> clear navigation.</li>
    <li>The blog has to be formal and factual, information on the site has to be easily accessibile to the user.</li>
    <li>The option of customizing the blog posts by the owner has to be limited ot the authorisation. A random user of the blog can not have permition to comment or post on the blog.</li>
    <li> As the topics discussed on the site contain sensitive information,I want the admin to be able to choose what comments get posted or not.
</ul>

### User Stories

### First time and Recurring Stories
<ol>
    <li>As a user of the site, I want to be able to Browse through content on the website.</li>
    <li>As a user of the site, I want to be able to View Court News Stories.</li>
    <li>As a user of the site, I want to be able to View Court News Stories in a List.</li>
    <li>As a user of the site, I want to be able to open and read the court news stories.</li>
    <li>As a user of the site, I want to be able to View comments under each post.</li>
    <li>As an authorized user of the site, I want to be able to Post Comments. </li>
    <li>As a user of the site, I want to be able to Register for an account.</li>
</ol>

### Site's Owner Stories
<ol>
    <li>As an authorized owner of the site, I want to be able to Post Stories to the site.</li>
    <li>As an authorized owner of the site, I want to be able to Create story drafts to come back to.</li>
    <li>As an authorized owner of the site, I want to be able to Manage site content.</li>
    <li>As an authorized owner of the site, I want to be able to Manage comments under posts.</li>
</ol>

## Technical Design

### Flow Chart
<p> I used the flow chart to design a clear map of my site that would help me design the functionality of the site and the logic and guidence for user stories. I did this by using Lucid Chart</p>
<details><summary>Flow Chart</summary>
        <img src="docs/flowchart/flowchart.jpeg"></details>
<hr>

### Database 
<p> My Database has three models:
<p> My project uses the relational databse -> PostgreSQL.</p>
<p> The data is handeled within the application with Django. </p>
<ul>
<li> Profile </li>
<li> Post </li>
<li> Comment </li>
<li> ---- </li>
</ul></p>
<p> Post and Comment have a many to one relationship and also uses the imported User class model for username and user unigue passwords.</p>
<details><summary>Database Diagram</summary>
        <img src="docs/flowchart/flowchart.jpeg"></details>
<br/>

### User Manual:
<ol>
<li>---</li>
<li> ----</li>
<li>----</li>
<li> ----</li>
<li> ----</li>
</ol>

### Wireframes:

<details><summary>Home Page</summary>
        <img src="docs/wireframes/home.png"></details>

<details><summary>Home Page: Membership Option</summary>
        <img src="docs/wireframes/home-member.png"></details>

<details><summary>Login</summary>
        <img src="docs/wireframes/login.png"></details>

<details><summary>Register</summary>
        <img src="docs/wireframes/register.png"></details>

<details><summary>Home page: Loggined-In User</summary>
        <img src="docs/wireframes/home-logged-in-user.png"></details>

<details><summary>Blog Post</summary>
        <img src="docs/wireframes/blog-post.png"></details>

<details><summary>Blog Post: Edit</summary>
            <img src="docs/wireframes/update-post.png"></details>

<details><summary>Blog Post: Delete</summary>
            <img src="docs/wireframes/delete-post.png"></details>

<details><summary>Blog Post: Create</summary>
            <img src="docs/wireframes/create-post.png"></details>

        

### Technology:

### Develpoment Languages Used

<ul>
<li> Python </li>
</ul>

###  Frameworks and Tools used
<ul>
<li> Git, GitHUb, and GitPod </li>
<li> Lucid Chart </li>
<li> Heroku </li>
<li> Django </li>
<li> BootStap </li>
</ul>

### 3rd Party Libraries:
<ul>
<li>------</li>
<li>------</li>
</ul>
<hr>

## Features:
<p>----</p>

### Home

<ul>
    <li>------</li>
</ul>
 <p>User Stories covered : -</p>
 <p>Site Owner's Stories covered: -</p>
        <details><summary>Home</summary>
        <img src="-"></details>

#### Game
<ul>
    <li>----</li>
    <li> ----</li>
    <li> ----</li>
    <li> ----</li>
    <li> ----<li>
</ul>
    <p> User Stories covered: -</p>
    <p>Site Owner's Stories covered: -</p>
        <details><summary>----</summary>
        <img src=""></details>
        <details><summary>----</summary>
        <img src=""></details>
        <details><summary>----</summary>
        <img src=""></details>
<hr>

## Testing:

### Python Validation
<p> To Validate my Python I used the PEP8 Online Validation Service. All python code passed its Validation with no errors but one warnings as shown below in the pictures.</p>

<details><summary>-</summary>
<img src=""></details>

<details><summary>-</summary>
<img src=""></details>

<hr>

### Testing User Stories

    1."--"
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|

<details><summary>User Testing 1</summary>
<img src="docs/flow_chart/features/game_play.png">
</details>
<hr>

    2."."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|

<details><summary>User Testing 2</summary>
<img src="docs/flow_chart/features/game_play.png">
</details>
<hr>

    3."."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|

<details><summary>User Testing 3</summary>
<img src="docs/flow_chart/features/intro_screen.png"></details>
<hr>

    4.""
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|

<details><summary>User Testing 4</summary>
<img src="docs/flow_chart/features/intro_screen.png">
<img src="docs/flow_chart/features/game_play.png">
<img src="docs/flow_chart/features/loser_screen.png">
<img src="docs/flow_chart/features/winner_screen.png"></details>
<hr>

    5.""
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|

<details><summary>User Testing 5</summary>
<img src="docs/flow_chart/features/game_feedback.png"></details>

<hr>

    6.""
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|

<details><summary>User Testing 6</summary>
<img src="docs/flow_chart/features/game_feedback.png"></details>

### Testing Site Owner's Stories

    1.""
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|

<details><summary>User Testing 7</summary>
<img src="docs/flow_chart/features/intro_screen.png"></details>
<hr>

    2.""
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|


<details><summary>User Testing 8</summary>
<img src="docs/flow_chart/features/game_play.png">
</details>
<hr>

    3.""
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|

<details><summary>User Testing 9</summary>
<img src="docs/flow_chart/features/intro_screen.png">
<img src="docs/flow_chart/features/game_play.png">
<img src="docs/flow_chart/features/loser_screen.png">
<img src="docs/flow_chart/features/winner_screen.png">
</details>
<hr>

    4.""
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|

<details><summary>User Testing 10</summary>
<img src="docs/flow_chart/features/game_feedback.png"></details>
<hr>

## Bugs:

| **Bug** | **Fix** |
<p> I have not found any bugs in my code.</p>
<hr>

## Deployment:
<p>In order to deploy my site I took the following steps using GitHub pages and Heroku:</p>

<ol>
<li> Clone or Fork my repository.</li>
<li> Create an account in the Heroku app, and within that create a new app.</li>
<li> Add a "Config Var" with a key 'PORT' and value '8000' in Heroku's settings.</li>
<li> Add buildbacks firstly for the python code, and then again for NodeJS.</li>
<li> Then link the app to the repository using the following steps:</li>
<ul>
<li>Manually - Click to deploy branch </li><br>
<p>or</p>
<li>Enable automatic deploys and follow the prompted instructions.</li>
</ul>
</ol>
<p> My link is: https://ci-pp3-hangman.herokuapp.com/ </p>
<hr>

<p> Forking the repository is done by the following steps:</p>
<ol>
<li>Within the GitHub repository, click "Fork" (a button) at the upper right hand corner.</li></ol>
<hr>
<p> Cloning the repository is done by the following steps:</p>
<ol>
<li>Within the GitHub repository, locate "Code" (a button) found at the top of the page.</li>
<li> Once selected, select which you prefere out of the following choise: HTTPS, SSH or GitHub CLI and press the copy URL to your clipboard.</li>
<li> Then open Git Bash.</li>
<li> Change the current directory to your desired location for the cloned directory.</li>
<li>Finally, type "git clone" and paste your URL.</li>
<li>Once you press enter your local clone is created.</li></ol>

## Credits:
### Source Code Used in Site

<p> Due to limitations in my knowledge I used youtube tutorials/ stack overflow articles to guide me with creating the game:</p>
<ul>
<li></li>
<li></li>
<li></li>
</ul>
<p> I used these videos/ articles soley as a guide I did not copy and paste.</p>
<ul><li> Photos :Photo by Tarzine Jackson from Pexels</li>

<>
<hr>

## Acknowledgements:
<p> I would like to take this oppurtuinity to thank and acknowlege the following people:
<ul>
<li> I would like to thank Mo Shami - my mentor - for his feedback and guidence whilst creating the project.</li>
<li> I would like to thank those on the code institute slack channel for help with any issues I had.</li>
<li> I would also like to thank Conor lawton who helped me with understanding some of the code.</li>
</ul>

## Future Features
<p>--</p>
