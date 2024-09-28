import LineChart from "./lineChart";

const WheelGroup = ({commands}) => {

    return <div className="wheel-group-container">
        <LineChart commands={commands} name="LeftWheels" id="3"/>
        <LineChart commands={commands} name="RightWheels" id="0"/>
    </div>
};
export default WheelGroup