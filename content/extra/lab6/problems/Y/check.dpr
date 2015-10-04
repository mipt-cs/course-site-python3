uses testlib,SysUtils;
const maxn = 10;
      maxc = 100000;
var p:array [1..maxn] of boolean;   
    n,t,ml,cn:longint;
begin
 fillchar(p,sizeof(p),0);
 n:=inf.readlongint;
 cn:=0;
 while not ouf.seekeof do
  begin
  inc(cn);
  if cn>maxc then quit(_pe,'Too many commands');
  t:=ouf.readlongint;
  if (t=0) or (abs(t)>n) then quit(_pe,'Cell does not exist');
  ml:=1;
  while (ml<=n) and (not p[ml]) do inc(ml);
  if (ml>n) then ml:=MaxLongint;
  if (abs(t)<>1) and (abs(t)<>ml+1) then quit(_wa,format('Operation with unavailable cell at command #%d',[cn]));
  if p[abs(t)] and (t>0) then quit(_wa,format('Cell is already occupied at command #%d',[cn])) else
   if (not p[abs(t)]) and (t<0) then quit(_wa,format('Cell is already empty at command #%d',[cn]));
  p[abs(t)]:=not p[abs(t)];
  end;
 for ml:=1 to n do
  if not p[ml] then quit(_wa,'After all commands row is not filled');
 quit(_ok,'Looks like correct');
end.