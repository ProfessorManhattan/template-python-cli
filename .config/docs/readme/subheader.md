<div align="center">
  <a href="{{ link.home }}" title="{{ organization }} homepage" target="_blank">
    <img alt="Homepage" src="https://img.shields.io/website?down_color=%23FF4136&down_message=Down&label=Homepage&logo=home-assistant&logoColor=white&up_color=%232ECC40&up_message=Up&url=https%3A%2F%2Fmegabyte.space&style={{ badge_style }}" />
  </a>
  <a href="https://pypi.org/user/{{profile.pypi}}/" title="PyPi profile" target="_blank">
    <img alt="PyPi" src="https://img.shields.io/badge/PyPi-000000?logo=pypi&logoColor=white&style={{ badge_style }}" />
  </a>
  <a href="https://pypi.org/project/{{(if customPyPiPackageName customPyPiPackageName (append repository.prefix.github slug))}}/" title="{{ name }} role on PyPi" target="_blank">
    <img alt="PyPi" src="https://img.shields.io/badge/PyPi-3775A9?logo=pypi&logoColor=white&style={{ badge_style }}" />
  </a>
  <a href="{{ repository.github }}{{ repository.location.contributing.github }}" title="Learn about contributing" target="_blank">
    <img alt="Contributing" src="https://img.shields.io/badge/Contributing-Guide-0074D9?logo=github-sponsors&logoColor=white&style={{ badge_style }}" />
  </a>
  <a href="{{ profile_link.patreon }}/{{ profile.patreon }}" title="Support us on Patreon" target="_blank">
    <img alt="Patreon" src="https://img.shields.io/badge/Patreon-Support-052d49?logo=patreon&logoColor=white&style={{ badge_style }}" />
  </a>
  <a href="{{ link.chat }}" title="Chat with us on Slack" target="_blank">
    <img alt="Slack" src="https://img.shields.io/badge/Slack-Chat-e01e5a?logo=slack&logoColor=white&style={{ badge_style }}" />
  </a>
  <a href="{{ repository.github }}" title="GitHub mirror" target="_blank">
    <img alt="GitHub" src="https://img.shields.io/badge/Mirror-GitHub-333333?logo=github&style={{ badge_style }}" />
  </a>
  <a href="{{ repository.gitlab }}" title="GitLab repository" target="_blank">
    <img alt="GitLab" src="https://img.shields.io/badge/Repo-GitLab-fc6d26?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgAQMAAABJtOi3AAAABlBMVEUAAAD///+l2Z/dAAAAAXRSTlMAQObYZgAAAHJJREFUCNdNxKENwzAQQNEfWU1ZPUF1cxR5lYxQqQMkLEsUdIxCM7PMkMgLGB6wopxkYvAeI0xdHkqXgCLL0Beiqy2CmUIdeYs+WioqVF9C6/RlZvblRNZD8etRuKe843KKkBPw2azX13r+rdvPctEaFi4NVzAN2FhJMQAAAABJRU5ErkJggg==&style={{ badge_style }}" />
  </a>
</div>
<br/>
<div align="center">
  <a title="Version: {{ pkg.version }}" href="{{ repository.github }}" target="_blank">
    <img alt="Version: {{ pkg.version }}" src="https://img.shields.io/badge/version-{{ pkg.version }}-blue.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgAQMAAABJtOi3AAAABlBMVEUAAAD///+l2Z/dAAAAAXRSTlMAQObYZgAAACNJREFUCNdjIACY//+BEp9hhM3hAzYQwoBIAqEDYQrCZLwAAGlFKxU1nF9cAAAAAElFTkSuQmCC&cacheSeconds=2592000&style={{ alt_badge_style }}" />
  </a>
  <a title="Build status on GitLab" href="{{ repository.gitlab }}{{ repository.location.commits.gitlab }}" target="_blank">
    <img alt="GitLab build status" src="https://img.shields.io/gitlab/pipeline-status/{{ repository.group.python_cli_path }}/{{ slug }}?branch=master&label=Build&logo=gitlab&style={{ alt_badge_style }}">
  </a>
  <a title="Test coverage report" href="{{ repository.gitlab }}{{ repository.location.commits.gitlab }}" target="_blank">
    <img alt="Coverage status" src="https://img.shields.io/gitlab/coverage/{{ repository.group.python_cli_path }}/{{ slug }}/master/?label=Coverage&logo=pytest&style={{ alt_badge_style }}">
  </a>
  <a title="Documentation" href="{{ link.docs }}/{{ group }}" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg?logo=readthedocs&style={{ alt_badge_style }}" />
  </a>
  <a title="Supported Python versions" href="https://pypi.org/project/{{(if customPyPiPackageName customPyPiPackageName (append repository.prefix.github slug))}}/" target="_blank">
    <img alt="Python versions" src="https://img.shields.io/pypi/pyversions/{{(if customPyPiPackageName customPyPiPackageName (append repository.prefix.github slug))}}/?label=Python&logo=python&style={{ alt_badge_style }}">
  </a>
  <a title="PyPi status" href="https://pypi.org/project/{{(if customPyPiPackageName customPyPiPackageName (append repository.prefix.github slug))}}/" target="_blank">
    <img alt="Status" src="https://img.shields.io/pypi/status/{{(if customPyPiPackageName customPyPiPackageName (append repository.prefix.github slug))}}/?label=Status&logo=pypi&style={{ alt_badge_style }}">
  </a>
  <a title="License: {{ license }}" href="{{ repository.github }}{{ repository.location.license.github }}" target="_blank">
    <img alt="License: {{ license }}" src="https://img.shields.io/badge/license-{{ license }}-yellow.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgAQMAAABJtOi3AAAABlBMVEUAAAD///+l2Z/dAAAAAXRSTlMAQObYZgAAAHpJREFUCNdjYOD/wMDAUP+PgYHxhzwDA/MB5gMM7AwMDxj4GBgKGGQYGCyAEEgbMDDwAAWAwmk8958xpIOI5zKH2RmOyhxmZjguAiKmgIgtQOIYmFgCIp4AlaQ9OczGkJYCJEAGgI0CGwo2HmwR2Eqw5SBnNIAdBHYaAJb6KLM15W/CAAAAAElFTkSuQmCC&style={{ alt_badge_style }}" />
  </a>
  <a title="Support us on Open Collective" href="{{ profile_link.opencollective }}/{{ profile.opencollective }}" target="_blank">
    <img alt="Open Collective sponsors" src="https://img.shields.io/opencollective/sponsors/megabytelabs?logo=opencollective&label=OpenCollective&logoColor=white&style={{ alt_badge_style }}" />
  </a>
  <a title="Support us on GitHub" href="{{ profile_link.github }}/{{ profile.github }}" target="_blank">
    <img alt="GitHub sponsors" src="https://img.shields.io/github/sponsors/{{ profile.github }}?label=GitHub%20sponsors&logo=github&style={{ alt_badge_style }}" />
  </a>
  <a title="Follow us on GitHub" href="{{ profile_link.github }}/{{ profile.github }}" target="_blank">
    <img alt="GitHub: {{ profile.github }}" src="https://img.shields.io/github/followers/{{ profile.github }}?style=social" target="_blank" />
  </a>
  <a title="Follow us on Twitter" href="https://twitter.com/{{ profile.twitter }}" target="_blank">
    <img alt="Twitter: {{ profile.twitter }}" src="https://img.shields.io/twitter/url/https/twitter.com/{{ profile.twitter }}.svg?style=social&label=Follow%20%40{{ profile.twitter }}" />
  </a>
</div>
