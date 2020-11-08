#!/usr/bin/env bash
echo "Creating database..."
createuser -s bridgenet_payment || :
createdb -O bridgenet_payment bridgenet_payment || :