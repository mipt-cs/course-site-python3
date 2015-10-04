program hanoi;
{$APPTYPE CONSOLE}
var n:longint;

procedure gen(const v,a,b:longint);
begin
 if (a+b=4) then
  begin
  gen(v,a,6-a-b);
  gen(v,6-a-b,b);
  end
 else if v=1 then writeln('1 ',a,' ',b)
 else
  begin
  gen(v-1,a,6-a-b);
  writeln(v,' ',a,' ',b);
  gen(v-1,6-a-b,b);
  end;
end;

begin
 read(n);
 gen(n,1,3);
end.
