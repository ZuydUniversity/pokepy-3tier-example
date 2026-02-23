#!/bin/sh
if [ -z "$husky_skip_init" ]; then
  debug () {
    [ "$HUSKY_DEBUG" = "1" ] && echo "husky (debug) - $1"
  }

  readonly hook_name="$(basename "$0")"
  debug "starting $hook_name..."

  if [ -f "$(dirname "$0")/../../.husky/.env" ]; then
    debug "sourcing .husky/.env"
    . "$(dirname "$0")/../../.husky/.env"
  fi

  export husky_skip_init=1
  sh -e "$(dirname "$0")/$hook_name"
  exitCode=$?

  if [ $exitCode != 0 ]; then
    echo "husky - $hook_name hook exited with code $exitCode (error)"
  fi

  if [ $exitCode = 127 ]; then
    echo "husky - $hook_name hook not found (skipping)"
    exit 0
  fi

  exit $exitCode
fi
