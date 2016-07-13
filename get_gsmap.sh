wget -nd -r -nc --no-parent -P LOCALDIR -A gz ftp://rainmap:Niskur+1404@hokusai.eorc.jaxa.jp/realtime/archive/
gunzip -k LOCALDIR/*.gz
