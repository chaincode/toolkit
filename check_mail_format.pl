# The script can check the format of a mail
# usage:
# 		perl check_mail_format.pl
#

print "Enter a mail for testing : \n";
$input = <STDIN>;
chomp($input);

$UsernameRegex = qr/[-a-z0-9]+/;
$HostnameRegex = qr/[-a-z0-9]+(\.[-a-z0-9]+)*\.(com|edu|gov|int|net|mil|org|biz|info|name|coop|[a-z]+)/;

if ($input =~ m{
	$UsernameRegex
	\@
	$HostnameRegex
	}gix
){
	print "mail[$input]is correct!\n";

}else{
	print "mail($input)is wrong!\n";
}

   

