# 🧠 PR Reviewer – Claude-Powered GitHub PR Review System

A Python-based intelligent tool to **automate pull request analysis** using the [Model Context Protocol (MCP)](https://modelcontextprotocol.io), developed by Anthropic. This system seamlessly integrates GitHub, Claude Desktop, and Notion to simplify and accelerate code review processes in modern development workflows.

## 🚀 Overview

Code reviews are critical but time-consuming. This system enables **Claude** to act as an autonomous PR reviewer via MCP, fetching code diffs, analyzing changes, and optionally documenting results in Notion.

Inspired by the guide by [Bhavik Jikadara](https://medium.com/@bhavikjikadara), this project shows how to set up an end-to-end Claude-powered review workflow.

## ✨ Features

- 🔁 Automatically fetch pull request changes via GitHub API
- 🧠 Claude Desktop integration using MCP for structured analysis
- 🧾 Optional Notion logging of PR summaries
- ⚙️ MCP server setup using `fastmcp` and CLI tools
- 🧪 Modular Python structure for extensions or integration with CI/CD

---
## Demo


<p align="center">
  <img src="demo6.gif" alt="Demo GIF" style="max-width:100%; height:auto;">
</p>

![https://youtu.be/zzgMfgQwXwU](https://youtu.be/zzgMfgQwXwU)

## 🛠️ How It Works

### Architecture

```text
+-------------+     MCP Protocol     +------------------+
| Claude App  | <------------------> |   MCP Server     |
| (AI agent)  |                      |  (this repo)      |
+-------------+                      +--------+----------+
                                              |
                                              | GitHub API
                                              |
                                       +------v------+
                                       | GitHub Repo |
                                       +-------------+
                                              |
                                              | Notion API
                                              |
                                       +------v------+
                                       |   Notion    |
                                       +-------------+ ```


