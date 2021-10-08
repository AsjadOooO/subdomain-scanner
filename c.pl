if($response =~/> (.*?) visitors per day </)
    {
        print item(),"Hosting Info for Website: $site1\n";
        print item(),"Visitors per day: $1 \n";

        if($response =~/> (.*?) visitors per day on (.*?)</){
            print item(),"Visitors per day: $1 \n";
        }
        $ip= (gethostbyname($site1))[4];
        my ($a,$b,$c,$d) = unpack('C4',$ip);
        $ip_address ="$a.$b.$c.$d";
        print item(),"IP Address: $ip_address\n";

        else
        {
            print item(), "Didn't found it $https\n";
            }
