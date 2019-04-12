<h1> Your Tunes </h1>
%for file in files:
    <div>
        <a href="./{{file}}">{{file}}</a>
    </div>
%end

<style>
    div {
        border-bottom: 1px solid black;
        padding: 5px;
    }

</style>