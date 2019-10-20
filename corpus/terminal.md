Welcome to the Windows Terminal, Console and Command-Line repo
This repository contains the source code for:

Windows Terminal
The Windows console host (conhost.exe)
Components shared between the two projects
ColorTool
Sample projects that show how to consume the Windows Console APIs

Related repositories include:

Console API Documentation
Cascadia Code Font

Installing & running Windows Terminal

👉 Note: Windows Terminal requires Windows 10 1903 (build 18362) or later

Manually install builds from this repository
For users who are unable to install Terminal from the Microsoft Store, Terminal builds can be manually downloaded from this repository's Releases page.

⚠ Note: If you install Terminal manually:

Be sure to install the Desktop Bridge VC++ v14 Redistributable Package otherwise Terminal may not install and/or run and may crash at startup
Terminal will not auto-update when new builds are released so you will need to regularly install the latest Terminal release to receive all the latest fixes and improvements!


Install via Chocolatey (unofficial)
Chocolatey users can download and install the latest Terminal release by installing the microsoft-windows-terminal package:
choco install microsoft-windows-terminal
To upgrade Windows Terminal using Chocolatey, run the following:
choco upgrade microsoft-windows-terminal
If you have any issues when installing/upgrading the package please go to the Windows Terminal package page and follow the Chocolatey triage process

Project Build Status



Project
Build Status




Terminal



ColorTool





Windows Terminal v1.0 Roadmap
The plan for delivering Windows Terminal v1.0 is described here, and will be updated as the project proceeds.

Terminal & Console Overview
Please take a few minutes to review the overview below before diving into the code:
Windows Terminal
Windows Terminal is a new, modern, feature-rich, productive terminal application for command-line users. It includes many of the features most frequently requested by the Windows command-line community including support for tabs, rich text, globalization, configurability, theming & styling, and more.
The Terminal will also need to meet our goals and measures to ensure it remains fast and efficient, and doesn't consume vast amounts of memory or power.
The Windows Console Host
The Windows Console host, conhost.exe, is Windows' original command-line user experience. It also hosts Windows' command-line infrastructure and the Windows Console API server, input engine, rendering engine, user preferences, etc. The console host code in this repository is the actual source from which the conhost.exe in Windows itself is built.
Since taking ownership of the Windows command-line in 2014, the team added several new features to the Console, including background transparency, line-based selection, support for ANSI / Virtual Terminal sequences, 24-bit color, a Pseudoconsole ("ConPTY"), and more.
However, because Windows Console's primary goal is to maintain backward compatibility, we have been unable to add many of the features the community (and the team) have been wanting for the last several years including tabs, unicode text, and emoji.
These limitations led us to create the new Windows Terminal.

You can read more about the evolution of the command-line in general, and the Windows command-line specifically in this accompanying series of blog posts on the Command-Line team's blog.

Shared Components
While overhauling Windows Console, we modernized its codebase considerably, cleanly separating logical entities into modules and classes, introduced some key extensibility points, replaced several old, home-grown collections and containers with safer, more efficient STL containers, and made the code simpler and safer by using Microsoft's Windows Implementation Libraries - WIL.
This overhaul resulted in several of Console's key components being available for re-use in any terminal implementation on Windows. These components include a new DirectWrite-based text layout and rendering engine, a text buffer capable of storing both UTF-16 and UTF-8, a VT parser/emitter, and more.
Creating the new Windows Terminal
When we started planning the new Windows Terminal application, we explored and evaluated several approaches and technology stacks. We ultimately decided that our goals would be best met by continuing our investment in our C++ codebase, which would allow us to reuse several of the aforementioned modernized components in both the existing Console and the new Terminal. Further, we realized that this would allow us to build much of the Terminal's core itself as a reusable UI control that others can incorporate into their own applications.
The result of this work is contained within this repo and delivered as the Windows Terminal application you can download from the Microsoft Store, or directly from this repo's releases.

Resources
For more information about Windows Terminal, you may find some of these resources useful and interesting:

Command-Line Blog
Command-Line Backgrounder Blog Series
Windows Terminal Launch: Terminal "Sizzle Video"
Windows Terminal Launch: Build 2019 Session
Run As Radio: Show 645 - Windows Terminal with Richard Turner
Azure Devops Podcast: Episode 54 - Kayla Cinnamon and Rich Turner on DevOps on the Windows Terminal


FAQ
I built and ran the new Terminal, but it looks just like the old console
Cause: You're launching the incorrect solution in Visual Studio.
Solution: Make sure you're building & deploying the CascadiaPackage project in Visual Studio.

⚠ Note: OpenConsole.exe is just a locally-built conhost.exe, the classic Windows Console that hosts Windows' command-line infrastructure. OpenConsole is used by Windows Terminal to connect to and communicate with command-line applications (via ConPty).


Documentation
All project documentation is located in the ./doc folder. If you would like to contribute to the documentation, please submit a pull request.

Contributing
We are excited to work alongside you, our amazing community, to build and enhance Windows Terminal!
BEFORE you start work on a feature/fix, please read & follow our Contributor's Guide to help avoid any wasted or duplicate effort.
Communicating with the Team
The easiest way to communicate with the team is via GitHub issues.
Please file new issues, feature requests and suggestions, but DO search for similar open/closed pre-existing issues before creating a new issue.
If you would like to ask a question that you feel doesn't warrant an issue (yet), please reach out to us via Twitter:

Kayla Cinnamon, Program Manager: @cinnamon_msft
Rich Turner, Program Manager: @richturn_ms
Dustin Howett, Engineering Lead: @dhowett
Michael Niksa, Senior Developer: @michaelniksa
Mike Griese, Developer: @zadjii
Carlos Zamora, Developer: @cazamor_msft

Developer Guidance
Prerequisites

You must be running Windows 1903 (build >= 10.0.18362.0) or later to run Windows Terminal
You must enable Developer Mode in the Windows Settings app to locally install and run Windows Terminal
You must have the Windows 10 1903 SDK installed
You must have at least VS 2019 installed
You must install the following Workloads via the VS Installer. Note: Opening the solution in VS 2019 will prompt you to install missing components automatically:

Desktop Development with C++
Universal Windows Platform Development
The following Individual Components

C++ (v142) Universal Windows Platform Tools





Building the Code
This repository uses git submodules for some of its dependencies. To make sure submodules are restored or updated, be sure to run the following prior to building:
git submodule update --init --recursive
OpenConsole.sln may be built from within Visual Studio or from the command-line using a set of convenience scripts & tools in the /tools directory:
Building in PowerShell
Import-Module .\tools\OpenConsole.psm1
Set-MsBuildDevEnvironment
Invoke-OpenConsoleBuild
Building in Cmd
.\tools\razzle.cmd
bcz
Debugging Terminal
To debug Terminal in VS, right click on CascadiaPackage (in the Solution Explorer) and go to properties. In the Debug menu, change "Application process" and "Background task process" to "Native Only".
You should then be able to build & debug the Terminal project by hitting F5.
Debugging

To debug in VS, right click on CascadiaPackage (from VS Solution Explorer) and go to properties, in the Debug menu, change "Application process" and "Background task process" to "Native Only".

Coding Guidance
Please review these brief docs below about our coding practices.

👉 If you find something missing from these docs, feel free to contribute to any of our documentation files anywhere in the repository (or write some new ones!)

This is a work in progress as we learn what we'll need to provide people in order to be effective contributors to our project.

Coding Style
Code Organization
Exceptions in our legacy codebase
Helpful smart pointers and macros for interfacing with Windows in WIL


Code of Conduct
This project has adopted the Microsoft Open Source Code of Conduct.
For more information see the Code of Conduct FAQ or contact opencode@microsoft.com with any additional questions or comments.
