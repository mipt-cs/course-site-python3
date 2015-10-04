program chips;
{$APPTYPE CONSOLE}
var n,i:longint;

procedure turn_off(const v:longint); forward;

procedure turn_on(const v:longint);
begin
 if v=1 then write('1 ') else
  begin
  turn_on(v-1);
  write(v,' ');
  turn_off(v-1);
  end;
end;

procedure turn_off(const v:longint);
begin
 if v=1 then write('-1 ') else
  begin
  turn_on(v-1);
  write(-v,' ');
  turn_off(v-1);
  end;
end;

begin
 read(n);
 for i:=n downto 1 do turn_on(i)
end.
 