from __future__ import absolute_import

import logging

import click

import strephit
from strephit import commons

CLI_COMMANDS = {
    'annotation': strephit.annotation.cli.cli,
    'commons': strephit.commons.cli.cli,
    'corpus_analysis': strephit.corpus_analysis.cli.cli,
    'extraction': strephit.extraction.cli.cli,
    'web_sources_corpus': strephit.web_sources_corpus.cli.cli,
    'classification': strephit.classification.cli.cli,
    'side_projects': strephit.side_projects.cli.cli,
    'rule_based': strephit.rule_based.cli.cli,
}

logging.getLogger("requests").setLevel(logging.WARNING)


@click.group(commands=CLI_COMMANDS)
@click.pass_context
@click.option('--log-level', type=(unicode, click.Choice(commons.logging.LEVELS)), multiple=True)
@click.option('--cache-dir', type=click.Path(file_okay=False, resolve_path=True), default=None)
def cli(ctxm, log_level, cache_dir):
    commons.logging.setup()
    for module, level in log_level:
        commons.logging.setLogLevel(module, level)

    if cache_dir:
        commons.cache.BASE_DIR = cache_dir
