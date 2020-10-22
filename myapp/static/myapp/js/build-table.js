 document.write("<table border=1>")
2  for (row=1; row<=4; row++) {
3     document.write("<tr>")
4     for (col=1; col<=5; col++) {
5           document.write("<td>R" + row + "<br>C" + col + "</td>")
6      }
7      document.write("</tr>")
8 }
9 document.write("</table>")