// 둘만의 암호
class 155652 {
    @Test
    void _155652(){
        //given
        var res=_155652("aukks",	"wbqd",5	);
        //when
        assertEquals("happy",res);
        //then
    }
    public static String _155652(String s, String skip, int index) {
        StringBuilder answer= new StringBuilder();
        for (char c : s.toCharArray()){
            answer.append(changeChar(c,skip,index));
        }
        System.out.println(answer);
        return answer.toString();
    }
    public static char changeChar(char c,String skip,int index){
        int i=0;
        while (i<index){
            c=(char)(c+1);
            if (skip.indexOf(c)==-1){ //없을경우 한칸 증가한것으로 취급
                i+=1;
            }
            if (c>'z'){
                var next_c='a';
                while (skip.indexOf(next_c)!=-1){
                    next_c=(char)(next_c+1);
                }
                c=next_c;
            }
        }
        return c;
    }

}