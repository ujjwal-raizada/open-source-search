




Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine. For
more information on using Node.js, see the Node.js Website.
The Node.js project uses an open governance model. The
OpenJS Foundation provides support for the project.
This project is bound by a Code of Conduct.
Table of Contents

Support
Release Types

Download

Current and LTS Releases
Nightly Releases
API Documentation


Verifying Binaries


Building Node.js
Security
Contributing to Node.js
Current Project Team Members

TSC (Technical Steering Committee)
Collaborators
Release Keys



Support
Looking for help? Check out the
instructions for getting support.
Release Types

Current: Under active development. Code for the Current release is in the
branch for its major version number (for example,
v10.x). Node.js releases a new
major version every 6 months, allowing for breaking changes. This happens in
April and October every year. Releases appearing each October have a support
life of 8 months. Releases appearing each April convert to LTS (see below)
each October.
LTS: Releases that receive Long-term Support, with a focus on stability
and security. Every even-numbered major version will become an LTS release.
LTS releases receive 18 months of Active LTS support and a further 12 months
of Maintenance. LTS release lines have alphabetically-ordered codenames,
beginning with v4 Argon. There are no breaking changes or feature additions,
except in some special circumstances.
Nightly: Code from the Current branch built every 24-hours when there are
changes. Use with caution.

Current and LTS releases follow Semantic Versioning. A
member of the Release Team signs each Current and LTS release.
For more information, see the
Release README.
Download
Binaries, installers, and source tarballs are available at
https://nodejs.org/en/download/.
Current and LTS Releases
https://nodejs.org/download/release/
The latest directory is an
alias for the latest Current release. The latest-codename directory is an
alias for the latest release from an LTS line. For example, the
latest-carbon directory
contains the latest Carbon (Node.js 8) release.
Nightly Releases
https://nodejs.org/download/nightly/
Each directory name and filename contains a date (in UTC time) and the commit
SHA at the HEAD of the release.
API Documentation
Documentation for the latest Current release is at https://nodejs.org/api/.
Version-specific documentation is available in each release directory in the
docs subdirectory. Version-specific documentation is also at
https://nodejs.org/download/docs/.
Verifying Binaries
Download directories contain a SHASUMS256.txt file with SHA checksums for the
files.
To download SHASUMS256.txt using curl:
$ curl -O https://nodejs.org/dist/vx.y.z/SHASUMS256.txt
To check that a downloaded file matches the checksum, run
it through sha256sum with a command such as:
$ grep node-vx.y.z.tar.gz SHASUMS256.txt | sha256sum -c -
For Current and LTS, the GPG detached signature of SHASUMS256.txt is in
SHASUMS256.txt.sig. You can use it with gpg to verify the integrity of
SHASUM256.txt. You will first need to import
the GPG keys of individuals authorized to create releases. To
import the keys:
$ gpg --keyserver pool.sks-keyservers.net --recv-keys DD8F2338BAE7501E3DD5AC78C273792F7D83545D
See the bottom of this README for a full script to import active release keys.
Next, download the SHASUMS256.txt.sig for the release:
$ curl -O https://nodejs.org/dist/vx.y.z/SHASUMS256.txt.sig
Then use gpg --verify SHASUMS256.txt.sig SHASUMS256.txt to verify
the file's signature.
Building Node.js
See BUILDING.md for instructions on how to build Node.js from
source and a list of supported platforms.
Security
For information on reporting security vulnerabilities in Node.js, see
SECURITY.md.
Contributing to Node.js

Contributing to the project
Working Groups
Strategic Initiatives

Current Project Team Members
For information about the governance of the Node.js project, see
GOVERNANCE.md.
TSC (Technical Steering Committee)

addaleax -
Anna Henningsen <anna@addaleax.net> (she/her)
apapirovski -
Anatoli Papirovski <apapirovski@mac.com> (he/him)
BethGriggs -
Beth Griggs <Bethany.Griggs@uk.ibm.com> (she/her)
ChALkeR -
Сковорода Никита Андреевич <chalkerx@gmail.com> (he/him)
cjihrig -
Colin Ihrig <cjihrig@gmail.com> (he/him)
danbev -
Daniel Bevenius <daniel.bevenius@gmail.com> (he/him)
fhinkel -
Franziska Hinkelmann <franziska.hinkelmann@gmail.com> (she/her)
Fishrock123 -
Jeremiah Senkpiel <fishrock123@rocketmail.com>
gabrielschulhof -
Gabriel Schulhof <gabriel.schulhof@intel.com>
gireeshpunathil -
Gireesh Punathil <gpunathi@in.ibm.com> (he/him)
jasnell -
James M Snell <jasnell@gmail.com> (he/him)
joyeecheung -
Joyee Cheung <joyeec9h3@gmail.com> (she/her)
mcollina -
Matteo Collina <matteo.collina@gmail.com> (he/him)
mhdawson -
Michael Dawson <michael_dawson@ca.ibm.com> (he/him)
MylesBorins -
Myles Borins <myles.borins@gmail.com> (he/him)
sam-github -
Sam Roberts <vieuxtech@gmail.com>
targos -
Michaël Zasso <targos@protonmail.com> (he/him)
thefourtheye -
Sakthipriyan Vairamani <thechargingvolcano@gmail.com> (he/him)
tniessen -
Tobias Nießen <tniessen@tnie.de>
Trott -
Rich Trott <rtrott@gmail.com> (he/him)

TSC Emeriti

bnoordhuis -
Ben Noordhuis <info@bnoordhuis.nl>
chrisdickinson -
Chris Dickinson <christopher.s.dickinson@gmail.com>
evanlucas -
Evan Lucas <evanlucas@me.com> (he/him)
gibfahn -
Gibson Fahnestock <gibfahn@gmail.com> (he/him)
indutny -
Fedor Indutny <fedor.indutny@gmail.com>
isaacs -
Isaac Z. Schlueter <i@izs.me>
joshgav -
Josh Gavant <josh.gavant@outlook.com>
mscdex -
Brian White <mscdex@mscdex.net>
nebrius -
Bryan Hughes <bryan@nebri.us>
ofrobots -
Ali Ijaz Sheikh <ofrobots@google.com> (he/him)
orangemocha -
Alexis Campailla <orangemocha@nodejs.org>
piscisaureus -
Bert Belder <bertbelder@gmail.com>
rvagg -
Rod Vagg <r@va.gg>
shigeki -
Shigeki Ohtsu <ohtsu@ohtsu.org> (he/him)
TimothyGu -
Tiancheng "Timothy" Gu <timothygu99@gmail.com> (he/him)
trevnorris -
Trevor Norris <trev.norris@gmail.com>

Collaborators

addaleax -
Anna Henningsen <anna@addaleax.net> (she/her)
ak239 -
Aleksei Koziatinskii <ak239spb@gmail.com>
AndreasMadsen -
Andreas Madsen <amwebdk@gmail.com> (he/him)
antsmartian -
Anto Aravinth <anto.aravinth.cse@gmail.com> (he/him)
apapirovski -
Anatoli Papirovski <apapirovski@mac.com> (he/him)
aqrln -
Alexey Orlenko <eaglexrlnk@gmail.com> (he/him)
bcoe -
Ben Coe <bencoe@gmail.com> (he/him)
bengl -
Bryan English <bryan@bryanenglish.com> (he/him)
benjamingr -
Benjamin Gruenbaum <benjamingr@gmail.com>
BethGriggs -
Beth Griggs <Bethany.Griggs@uk.ibm.com> (she/her)
bmeck -
Bradley Farias <bradley.meck@gmail.com>
bmeurer -
Benedikt Meurer <benedikt.meurer@gmail.com>
bnoordhuis -
Ben Noordhuis <info@bnoordhuis.nl>
boneskull -
Christopher Hiller <boneskull@boneskull.com> (he/him)
brendanashworth -
Brendan Ashworth <brendan.ashworth@me.com>
BridgeAR -
Ruben Bridgewater <ruben@bridgewater.de> (he/him)
bzoz -
Bartosz Sosnowski <bartosz@janeasystems.com>
calvinmetcalf -
Calvin Metcalf <calvin.metcalf@gmail.com>
cclauss -
Christian Clauss <cclauss@me.com> (he/him)
ChALkeR -
Сковорода Никита Андреевич <chalkerx@gmail.com> (he/him)
cjihrig -
Colin Ihrig <cjihrig@gmail.com> (he/him)
claudiorodriguez -
Claudio Rodriguez <cjrodr@yahoo.com>
codebytere -
Shelley Vohr <codebytere@gmail.com> (she/her)
danbev -
Daniel Bevenius <daniel.bevenius@gmail.com> (he/him)
DavidCai1993 -
David Cai <davidcai1993@yahoo.com> (he/him)
davisjam -
Jamie Davis <davisjam@vt.edu> (he/him)
devnexen -
David Carlier <devnexen@gmail.com>
devsnek -
Gus Caplan <me@gus.host> (he/him)
digitalinfinity -
Hitesh Kanwathirtha <digitalinfinity@gmail.com> (he/him)
edsadr -
Adrian Estrada <edsadr@gmail.com> (he/him)
eljefedelrodeodeljefe -
Robert Jefe Lindstaedt <robert.lindstaedt@gmail.com>
eugeneo -
Eugene Ostroukhov <eostroukhov@google.com>
evanlucas -
Evan Lucas <evanlucas@me.com> (he/him)
fhinkel -
Franziska Hinkelmann <franziska.hinkelmann@gmail.com> (she/her)
Fishrock123 -
Jeremiah Senkpiel <fishrock123@rocketmail.com>
gabrielschulhof -
Gabriel Schulhof <gabriel.schulhof@intel.com>
gdams -
George Adams <george.adams@uk.ibm.com> (he/him)
geek -
Wyatt Preul <wpreul@gmail.com>
gengjiawen -
Jiawen Geng <technicalcute@gmail.com>
gibfahn -
Gibson Fahnestock <gibfahn@gmail.com> (he/him)
gireeshpunathil -
Gireesh Punathil <gpunathi@in.ibm.com> (he/him)
guybedford -
Guy Bedford <guybedford@gmail.com> (he/him)
hashseed -
Yang Guo <yangguo@chromium.org> (he/him)
hiroppy -
Yuta Hiroto <hello@hiroppy.me> (he/him)
iarna -
Rebecca Turner <me@re-becca.org>
imyller -
Ilkka Myller <ilkka.myller@nodefield.com>
indutny -
Fedor Indutny <fedor.indutny@gmail.com>
italoacasas -
Italo A. Casas <me@italoacasas.com> (he/him)
JacksonTian -
Jackson Tian <shyvo1987@gmail.com>
jasnell -
James M Snell <jasnell@gmail.com> (he/him)
jasongin -
Jason Ginchereau <jasongin@microsoft.com>
jbergstroem -
Johan Bergström <bugs@bergstroem.nu>
jdalton -
John-David Dalton <john.david.dalton@gmail.com>
jkrems -
Jan Krems <jan.krems@gmail.com> (he/him)
joaocgreis -
João Reis <reis@janeasystems.com>
joshgav -
Josh Gavant <josh.gavant@outlook.com>
joyeecheung -
Joyee Cheung <joyeec9h3@gmail.com> (she/her)
julianduque -
Julian Duque <julianduquej@gmail.com> (he/him)
JungMinu -
Minwoo Jung <nodecorelab@gmail.com> (he/him)
kfarnung -
Kyle Farnung <kfarnung@microsoft.com> (he/him)
kunalspathak -
Kunal Pathak <kunal.pathak@microsoft.com>
lance -
Lance Ball <lball@redhat.com> (he/him)
Leko -
Shingo Inoue <leko.noor@gmail.com> (he/him)
lpinca -
Luigi Pinca <luigipinca@gmail.com> (he/him)
lucamaraschi -
Luca Maraschi <luca.maraschi@gmail.com> (he/him)
lundibundi -
Denys Otrishko <shishugi@gmail.com> (he/him)
maclover7 -
Jon Moss <me@jonathanmoss.me> (he/him)
mafintosh
Mathias Buus <mathiasbuus@gmail.com> (he/him)
mcollina -
Matteo Collina <matteo.collina@gmail.com> (he/him)
mhdawson -
Michael Dawson <michael_dawson@ca.ibm.com> (he/him)
misterdjules -
Julien Gilli <jgilli@nodejs.org>
mmarchini -
Matheus Marchini <mat@mmarchini.me>
MoonBall -
Chen Gang <gangc.cxy@foxmail.com>
mscdex -
Brian White <mscdex@mscdex.net>
MylesBorins -
Myles Borins <myles.borins@gmail.com> (he/him)
not-an-aardvark -
Teddy Katz <teddy.katz@gmail.com> (he/him)
ofrobots -
Ali Ijaz Sheikh <ofrobots@google.com> (he/him)
oyyd -
Ouyang Yadong <oyydoibh@gmail.com> (he/him)
princejwesley -
Prince John Wesley <princejohnwesley@gmail.com>
psmarshall -
Peter Marshall <petermarshall@chromium.org> (he/him)
Qard -
Stephen Belanger <admin@stephenbelanger.com> (he/him)
refack -
Refael Ackermann (רפאל פלחי) <refack@gmail.com> (he/him/הוא/אתה)
richardlau -
Richard Lau <riclau@uk.ibm.com>
ronkorving -
Ron Korving <ron@ronkorving.nl>
RReverser -
Ingvar Stepanyan <me@rreverser.com>
rubys -
Sam Ruby <rubys@intertwingly.net>
rvagg -
Rod Vagg <rod@vagg.org>
ryzokuken -
Ujjwal Sharma <usharma1998@gmail.com> (he/him)
saghul -
Saúl Ibarra Corretgé <saghul@gmail.com>
sam-github -
Sam Roberts <vieuxtech@gmail.com>
santigimeno -
Santiago Gimeno <santiago.gimeno@gmail.com>
sebdeckers -
Sebastiaan Deckers <sebdeckers83@gmail.com>
seishun -
Nikolai Vavilov <vvnicholas@gmail.com>
shigeki -
Shigeki Ohtsu <ohtsu@ohtsu.org> (he/him)
shisama -
Masashi Hirano <shisama07@gmail.com> (he/him)
silverwind -
Roman Reiss <me@silverwind.io>
srl295 -
Steven R Loomis <srloomis@us.ibm.com>
starkwang -
Weijia Wang <starkwang@126.com>
targos -
Michaël Zasso <targos@protonmail.com> (he/him)
thefourtheye -
Sakthipriyan Vairamani <thechargingvolcano@gmail.com> (he/him)
thekemkid -
Glen Keane <glenkeane.94@gmail.com> (he/him)
thlorenz -
Thorsten Lorenz <thlorenz@gmx.de>
TimothyGu -
Tiancheng "Timothy" Gu <timothygu99@gmail.com> (he/him)
tniessen -
Tobias Nießen <tniessen@tnie.de>
trevnorris -
Trevor Norris <trev.norris@gmail.com>
trivikr -
Trivikram Kamat <trivikr.dev@gmail.com>
Trott -
Rich Trott <rtrott@gmail.com> (he/him)
vdeturckheim -
Vladimir de Turckheim <vlad2t@hotmail.com> (he/him)
vkurchatkin -
Vladimir Kurchatkin <vladimir.kurchatkin@gmail.com>
watilde -
Daijiro Wachi <daijiro.wachi@gmail.com> (he/him)
watson -
Thomas Watson <w@tson.dk>
XadillaX -
Khaidi Chu <i@2333.moe> (he/him)
yhwang -
Yihong Wang <yh.wang@ibm.com>
yorkie -
Yorkie Liu <yorkiefixer@gmail.com>
yosuke-furukawa -
Yosuke Furukawa <yosuke.furukawa@gmail.com>
ZYSzys -
Yongsheng Zhang <zyszys98@gmail.com> (he/him)

Collaborator Emeriti

andrasq -
Andras <andras@kinvey.com>
AnnaMag -
Anna M. Kedzierska <anna.m.kedzierska@gmail.com>
estliberitas -
Alexander Makarenko <estliberitas@gmail.com>
chrisdickinson -
Chris Dickinson <christopher.s.dickinson@gmail.com>
firedfox -
Daniel Wang <wangyang0123@gmail.com>
imran-iq -
Imran Iqbal <imran@imraniqbal.org>
isaacs -
Isaac Z. Schlueter <i@izs.me>
jhamhader -
Yuval Brik <yuval@brik.org.il>
lxe -
Aleksey Smolenchuk <lxe@lxe.co>
matthewloring -
Matthew Loring <mattloring@google.com>
micnic -
Nicu Micleușanu <micnic90@gmail.com> (he/him)
mikeal -
Mikeal Rogers <mikeal.rogers@gmail.com>
monsanto -
Christopher Monsanto <chris@monsan.to>
Olegas -
Oleg Elifantiev <oleg@elifantiev.ru>
orangemocha -
Alexis Campailla <orangemocha@nodejs.org>
othiym23 -
Forrest L Norvell <ogd@aoaioxxysz.net> (he/him)
petkaantonov -
Petka Antonov <petka_antonov@hotmail.com>
phillipj -
Phillip Johnsen <johphi@gmail.com>
piscisaureus -
Bert Belder <bertbelder@gmail.com>
pmq20 -
Minqi Pan <pmq2001@gmail.com>
rlidwka -
Alex Kocharin <alex@kocharin.ru>
rmg -
Ryan Graham <r.m.graham@gmail.com>
robertkowalski -
Robert Kowalski <rok@kowalski.gd>
romankl -
Roman Klauke <romaaan.git@gmail.com>
stefanmb -
Stefan Budeanu <stefan@budeanu.com>
tellnes -
Christian Tellnes <christian@tellnes.no>
tunniclm -
Mike Tunnicliffe <m.j.tunnicliffe@gmail.com>
vsemozhetbyt -
Vse Mozhet Byt <vsemozhetbyt@gmail.com> (he/him)
whitlockjc -
Jeremy Whitlock <jwhitlock@apache.org>

Collaborators follow the COLLABORATOR_GUIDE.md in
maintaining the Node.js project.
Release Keys
GPG keys used to sign Node.js releases:

Beth Griggs <bethany.griggs@uk.ibm.com>
4ED778F539E3634C779C87C6D7062848A1AB005C
Colin Ihrig <cjihrig@gmail.com>
94AE36675C464D64BAFA68DD7434390BDBE9B9C5
Evan Lucas <evanlucas@me.com>
B9AE9905FFD7803F25714661B63B535A4C206CA9
Gibson Fahnestock <gibfahn@gmail.com>
77984A986EBC2AA786BC0F66B01FBB92821C587A
James M Snell <jasnell@keybase.io>
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1
Jeremiah Senkpiel <fishrock@keybase.io>
FD3A5288F042B6850C66B31F09FE44734EB7990E
Michaël Zasso <targos@protonmail.com>
8FCCA13FEF1D0C2E91008E09770F7A9A5AE15600
Myles Borins <myles.borins@gmail.com>
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8
Rod Vagg <rod@vagg.org>
DD8F2338BAE7501E3DD5AC78C273792F7D83545D
Ruben Bridgewater <ruben@bridgewater.de>
A48C2BEE680E841632CD4E44F07496B3EB3C1762
Shelley Vohr <shelley.vohr@gmail.com>
B9E2F5981AA6E0CD28160D9FF13993A75599653C

To import the full set of trusted release keys:
gpg --keyserver pool.sks-keyservers.net --recv-keys 4ED778F539E3634C779C87C6D7062848A1AB005C
gpg --keyserver pool.sks-keyservers.net --recv-keys B9E2F5981AA6E0CD28160D9FF13993A75599653C
gpg --keyserver pool.sks-keyservers.net --recv-keys 94AE36675C464D64BAFA68DD7434390BDBE9B9C5
gpg --keyserver pool.sks-keyservers.net --recv-keys B9AE9905FFD7803F25714661B63B535A4C206CA9
gpg --keyserver pool.sks-keyservers.net --recv-keys 77984A986EBC2AA786BC0F66B01FBB92821C587A
gpg --keyserver pool.sks-keyservers.net --recv-keys 71DCFD284A79C3B38668286BC97EC7A07EDE3FC1
gpg --keyserver pool.sks-keyservers.net --recv-keys FD3A5288F042B6850C66B31F09FE44734EB7990E
gpg --keyserver pool.sks-keyservers.net --recv-keys 8FCCA13FEF1D0C2E91008E09770F7A9A5AE15600
gpg --keyserver pool.sks-keyservers.net --recv-keys C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8
gpg --keyserver pool.sks-keyservers.net --recv-keys DD8F2338BAE7501E3DD5AC78C273792F7D83545D
gpg --keyserver pool.sks-keyservers.net --recv-keys A48C2BEE680E841632CD4E44F07496B3EB3C1762
See the section above on Verifying Binaries for how to
use these keys to verify a downloaded file.
Other keys used to sign some previous releases:

Chris Dickinson <christopher.s.dickinson@gmail.com>
9554F04D7259F04124DE6B476D5A82AC7E37093B
Isaac Z. Schlueter <i@izs.me>
93C7E9E91B49E432C2F75674B0A78B0A6C481CF6
Italo A. Casas <me@italoacasas.com>
56730D5401028683275BD23C23EFEFE93C4CFFFE
Julien Gilli <jgilli@fastmail.fm>
114F43EE0176B71C7BC219DD50A3051F888C628D
Timothy J Fontaine <tjfontaine@gmail.com>
7937DFD2AB06298B2293C3187D33FF9D0246406D

