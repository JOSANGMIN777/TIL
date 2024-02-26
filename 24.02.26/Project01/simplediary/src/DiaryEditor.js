import { useState } from "react";

const DiaryEditor = () => { // 다이어리에디터 컴포넌트 생성
    const[state, setState] = useState({
        author: '',
        content: '',
        emotion: '',
    });

const ChangeState = (e) => {
    setState({
        ...state, // 바뀌는 값 제외한 나머지는 그대로 받아와야해서 
        [e.target.name] : e.target.value // name의 값을 새로운 input 값으로 업데이트
    });
}

const handleSubmit = () => {
    console.log(state)
    alert('대충 저장됐다는 말')
}

   return <div className="DiaryEditor">
    
        <div>
            <input 
            name="author"
            onChange={ChangeState}
            value={state.author} // useState안에 든 값들이 state의 초기값으로 설정됨 이후 값이 변함에 따라 변한값이 출력됨
            //onChange={(e)=> { // 입력이 e라는 매개변수에 들어옴
               // setState({ // state를 바꾸는 setState 콜백 함수 안에 인자를 넣어줌
                    //...state, // 간단하게 스프레드 연산자로 state불러오기
                    //author: e.target.value, // 점 표기법으로 데이터 저장
                    //content: state.content  // author 입력중이니까 content는 가만히 있어야지
               // })
           // }}
            />
            
        </div> 
        <div>
            <textarea
            name="content"
            value={state.content}
            onChange={ChangeState}
            //onChange={(e)=>{
                //setState({
                    //author: state.author,
                    //...state,   // !!!!!!! ...state의 위치에 따라 업데이트 값이 덮어씌워져서 아무 변동없는것처럼 보일 수 있으므로 순서중요
                   // content: e.target.value,
           // })
           // }}            
            />
        </div>
        <div>
            <select name="emotion" value={state.emotion} onChange={ChangeState}>
                <option value={1}>1</option>
                <option value={2}>2</option>
                <option value={3}>3</option>
                <option value={4}>4</option>
                <option value={5}>5</option>
            </select>
        </div>
            <button onClick={handleSubmit}>쌈@뽕하게 저장</button>
    </div>
}
export default DiaryEditor;