#!/bin/bash
# WANT_JSON

addr=$(cat $1 | grep -Po '(?<="addr": ")(.*?)(?=")')
tls=$(cat $1 | grep -Po '(?<="tls": )(.*?)(?=,)')


if [[ $tls == 'true' ]]
then
  addr="https://"$addr
else
  addr="http://"$addr
fi

#Request to host
info=$(curl -Isk $addr | head -1)
#info=$(/usr/bin/curl -k -I -o /dev/stdout --url $addr1 -m 2 -s )

# Result  
codest=$(echo "$info" | grep HTTP | tr -dc '[:print:]' )
# Code number
code=$(echo "$info" | grep HTTP | cut -d" " -f2 )

# Check results and return msg
if [[ $code == '200' ]]
then
echo '{"changed":false,"result_req":"'$codest'" }'
elif [[ $code ]]
then
echo '{"changed":false,"failed":true,"result_req":"'$codest'" }'
else
echo '{"changed":false,"failed":true,"result_req":"Host not response" }'
fi

