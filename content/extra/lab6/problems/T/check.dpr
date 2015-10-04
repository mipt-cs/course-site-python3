uses testlib,SysUtils;
const maxr = 3;
	  maxn = 10;
	  maxc = 200000;
var r:array [1..maxr,0..maxn] of longint;
	n,i,cc,ta,tb,tc:longint;
begin
 n:=inf.readlongint;
 r[1,0]:=n;
 for i:=1 to n do r[1,i]:=n-i+1;
 cc:=0;
 while not ouf.seekeof do
  begin
  inc(cc);
  if cc>maxc then quit(_pe,'Too many commands');
  ta:=ouf.readlongint;
  tb:=ouf.readlongint;
  tc:=ouf.readlongint;
  if (ta<1) or (ta>maxn) then quit(_pe,format('Wrong disk ID at command #%d',[cc]));
  if (tb<1) or (tb>maxr) then quit(_pe,format('Wrong rod ID at command #%d',[cc]));
  if (tc<1) or (tc>maxr) then quit(_pe,format('Wrong rod ID at command #%d',[cc]));
  if (tb=1) and (tc=maxr) then quit(_wa,format('Disk moving breaks the rules of the game at command #%d',[cc]));
  if (tc=1) and (tb=maxr) then quit(_wa,format('Disk moving breaks the rules of the game at command #%d',[cc]));
  if (r[tb,0]=0) then quit(_wa,format('Rod is empty at command #%d',[cc]));
  if (r[tb,r[tb,0]]<>ta) then quit(_wa,format('There is no disk #%d on rod #%d at command #%d',[ta,tb,cc]));
  if (r[tc,0]<>0) and (r[tc,r[tc,0]]<ta) then quit(_wa,format('Disk moving breaks the rules of the game at command #%d',[cc]));
  dec(r[tb,0]);
  inc(r[tc,0]);
  r[tc,r[tc,0]]:=ta
  end;
 if (r[maxr,0]<>n) then quit(_wa,'After all commands all rods are not on their places');
 quit(_ok,'Looks like correct');
end.
