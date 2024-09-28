import LineChart from "./lineChart";

const ArmGroup = ({commands}) => {

    return <div className="top-right-component">
        <LineChart commands={commands} name="Elbow" id="0"/>
        <LineChart commands={commands} name="Claw" id="3"/>
        <LineChart commands={commands} name="WristRight" id="1"/>
        <LineChart commands={commands} name="Gantry" id="4"/>
        <LineChart commands={commands} name="WristLeft" id="2"/>
        <LineChart commands={commands} name="Shoulder" id="5"/>
    </div>
};
export default ArmGroup
