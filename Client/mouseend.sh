#!/bin/bash

ps aux | grep 'remotemovemouse.py' | awk '{print $2}' | xargs kill -9
