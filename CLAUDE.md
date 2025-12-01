# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Advent of Code 2025 solutions repository using Python 3.12+ with uv for package management.

## Commands

- `uv run python main.py` - Run the main entry point
- `uv run ruff check --fix .` - Lint with auto-fix
- `uv run ruff format .` - Format code
- `pre-commit run --all-files` - Run all pre-commit hooks

## Configuration

Copy `.env.example` to `.env` and set:
- `SESSION_COOKIE` - Your Advent of Code session cookie (required for fetching puzzle inputs)
- `BASE_URL` - Defaults to `https://adventofcode.com`

## Architecture

- `client.py` - `AdventOfCodeClient` class for fetching puzzle inputs via httpx
- `main.py` - Main entry point
