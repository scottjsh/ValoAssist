<p align="center">
    <a href="https://github.com/scottjsh/ValoAssist/">
        <img src="assets/Logo.png" alt="Logo" width="160" height="160">
    </a>
<h5 align="center"> ValoAssist</h5>

[![Downloads][downloads-shield]][downloads-url]
    
 
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    <li><a href="#disclaimer">Disclaimer</a></li>
  </ol>

    
## About The Project

 ![Screenshot](assets/Example.png)
 ![Skin Showcase Image](assets/SkinShowcase.png)

|Their Queue|Current Skin|Current Rank|Rank Rating|Peak Rank|Account Level|
|:---:|:---:|:---:|:---:|:---:|:---:|
|![Parties](assets/Party.png)|![Skin](assets/Skin.png)|![Rank](assets/Rank.png)|![Rating](assets/Rating.png)|![Peak](assets/PeakRank.png)|![Level](assets/Level.png)|
    

## Usage
 **VALORANT must be open**.

### Bundled Release:

1) Download [Microsoft Visual C++ Libraries](https://github.com/abbodi1406/vcredist/releases)
2) Download the [release](https://github.com/scottjsh/ValAssist/releases/latest).
3) Extract **all** files.
4) Run VAS.exe.

### Running from source:

1) Download [Python 3.10](https://www.python.org/downloads/release/python-3100/), make sure it is added to the PATH. (This is an option on installation.)
   1) Any Python version post 3.10 should work.
2) Download the [source](https://github.com/scottjsh/ValAssist/archive/refs/heads/main.zip).
3) Open a terminal within the source folder.
4) `pip install -r requirements.txt`
5) `main.py`

### Compiling from source:

1) `pip install cx_Freeze`
2) `python setup.py build`
3)  Open the new Build folder and find VAS.exe.

> `-` You can change the desired weapon by editing the gun in `config.json`, or by deleting the file for VAS re-prompt you.

### Letting Github Build It:

The latest commits to the `main` branch will be built by a [Github Actions](https://github.com/scottjsh/ValAssist/actions) workflow 
and a successful build should result in a compiled artifact that you can download and try out.
See the [Actions tab](https://github.com/scottjsh/ValAssist/actions), click on the `Build` workflow, 
select a particular workflow run, and it should have an artifact available for download. 

If you want to make a small change to the application, you can:
1) [Fork](https://github.com/scottjsh/ValAssist/fork) this project.
2) Change the code in your forked repository.
3) Let the Github Actions workflow build VAS.exe for you.
4) Download it and test it.
5) Submit a Pull Request if you would like your change included in future releases.

## What about that Tweet?

 The [Tweet](https://twitter.com/PlayVALORANT/status/1539728676815642624), which details Riot's API policies, outlines how
 applications are not allowed to expose data hidden by the game client. As of Version 1.262, VAS respects streamer mode.

## Contributing

 Any contributions you make are **greatly appreciated**.

## Acknowledgements

 - [Valorant-API.com](https://valorant-api.com/)
 - [Hamper](https://hamper.dev/)
 - [D3CRYPT](https://d3crypt360.pages.dev/)
 
## Disclaimer

 THIS PROJECT IS NOT ASSOCIATED OR ENDORSED BY RIOT GAMES. Riot Games, and all associated properties are trademarks or registered trademarks of Riot Games, Inc.
    
 Whilst effort has been made to abide by Riot's API rules; you acknowledge that use of this software is done so at your own risk.


[downloads-shield]: https://img.shields.io/github/downloads/scottjsh/ValoAssist/total?style=for-the-badge&logo=github
[downloads-url]: https://github.com/scottjsh/ValoAssist/releases/latest
