
/* dao에서 받은 json 포맷의 문자열을 json 객체로 변환
demo의 위치에 table을 생성해서 직원수만큼 row를 구성해야 함
table의 row tag는 동일
    <tr><td>사번</td><td>이름</td><td>급여</td></tr>
ui는 똑같은데 데이터만 가변적이므로 반복문을 사용해서 json으로부터 값을 뽑는다
json에 직원 수부터 파악, 파악한 수만큼 반복을 돌리면 존재하는 데이터만큼 테이블 만들어짐 */

function empall() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            data = this.responseText;
            data = JSON.parse(data);

            tab = `
            <table border="1">
                <tr><th>사번</th><th>이름</th><th>급여</th></tr>`;

                let empno;
                let ename;
                let sal;

                for(no in data){
                    empno = data[no].empno;
                    ename = data[no].ename;
                    sal = data[no].sal;
                    // console.log(data[no].empno);   data[no]의 타입은 객체 object
                tab = tab + `<tr>
                    <td>${empno}</td>
                    <td>${ename}</td>
                    <td>${sal}</td>
                </tr>`;
                }
            tab = tab + `</table>`;
            // console.log(tab);
            document.getElementById("demo").innerHTML = tab;
        };
    };
    xhttp.open("GET", "emplist");
    xhttp.send();
}
