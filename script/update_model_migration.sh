#!/bin/bash
echo "开始"
cd ../wegame/data
read -p "请输入更新的相关信息" MIGRATIONSMSG
alembic revision --autogenerate -m "$MIGRATIONSMSG"
read -p "是否立即更新到数据库" ANSWER
case "$ANSWER" in
  [yY] | [yY][eE][sS])
    echo "开始更新"
    alembic upgrade head
    ;;
  [nN] | [nN][oO])
    echo "结束"
    ;;
  *)
    echo "Invalid Answer :/"
    ;;
esac
