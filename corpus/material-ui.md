


Material-UI

React components that implement Google's Material Design.















Installation
Material-UI is available as an npm package.
Stable channel v4
// with npm
npm install @material-ui/core

// with yarn
yarn add @material-ui/core
v3.x (Migration from v3 to v4)
v0.x (Migration to v1)
Please note that @next will only point to pre-releases; to get the latest stable release use @latest instead.
Supporting Material-UI
Material-UI is an MIT-licensed open source project. It's an independent project with ongoing development helped by the support of these awesome backers. If you'd like to join them, please consider:

Become a backer or sponsor on Patreon.
Become a backer or sponsor on OpenCollective.

What's the difference between Patreon and OpenCollective?
Funds donated via Patreon directly support Olivier Tassinari's work on Material-UI.
Funds donated via OpenCollective are managed transparently and will be used for compensating work and expenses for core team members.
Your name/logo will receive proper recognition and exposure by donating on either platform.
Gold Sponsors
Gold Sponsors are those who have pledged $500/month and more to Material-UI.
via Patreon






via OpenCollective



There is more!
See the full list of our backers.
Usage
Here is a quick example to get you started, it's all you need:
import React from 'react';
import ReactDOM from 'react-dom';
import Button from '@material-ui/core/Button';

function App() {
  return (
    <Button variant="contained" color="primary">
      Hello World
    </Button>
  );
}

ReactDOM.render(<App />, document.querySelector('#app'));
Yes, it's really all you need to get started as you can see in this live and interactive demo:

Questions
For how-to questions and other non-issues,
please use StackOverflow instead of Github issues.
There is a StackOverflow tag called "material-ui" that you can use to tag your questions.
Examples
Are you looking for an example project to get started?
We host some.
Documentation
Check out our documentation website.
Premium Themes
You can find complete templates & themes in our premium themes section.
Contributing
Read our contributing guide to learn about our development process, how to propose bugfixes and improvements, and how to build and test your changes to Material-UI.
Notice that contributions go far beyond pull requests and commits.
Although we love giving you the opportunity to put your stamp on Material-UI, we also are thrilled to receive a variety of other contributions.
Changelog
Recently Updated?
Please read the changelog.
Roadmap
The future plans and high priority features and enhancements can be found in the roadmap file.
Thanks
Material-UI is only made possible thanks to these great services that sponsor our core infrastructure:

GitHub allows us to host the Git repository.

CircleCI allows us to run the test suite.

Netlify allows us to distribute the documentation.

CrowdIn allows us to translate the documentation.

BrowserStack allows us to test in real browsers.

CodeCov allows us to monitor the test coverage.
License
This project is licensed under the terms of the
MIT license.
