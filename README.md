# auto-publish-release
Automatically Publish a release with a commit message of the following schema: `#RELEASE{major.minor.patch}`, e.g. `#RELEASE1.0.0`.
You need to put `<!-- CHANGELOG -->` before and after the changelog in your README file for this action to work.

With this setup, the action creates a release with a title of the version, adds a tag with the schema `major_minor_patch` and updates the CHANGELOG.

## Upcoming Version:
<!-- CHANGELOG -->

<!-- CHANGELOG -->
