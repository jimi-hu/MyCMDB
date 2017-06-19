function sys_info()
{
mem=`free -m | grep -i Mem | grep -v grep | awk '{print $2}'`
cpu=`cat /proc/cpuinfo  2>/dev/null| grep -i processor | grep -v grep | wc -l`
hostname=`hostname`
echo '{"mem":'"\"${mem}m\","'"cpu":'"$cpu,"'"hostname":'"\"$hostname\"}"
}

sys_info
