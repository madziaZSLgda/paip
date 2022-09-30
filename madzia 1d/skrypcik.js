var flash = 0
function lightning() {
    flash = flash + 1;
    if (flash == 1) { document.bgColor = 'white'; setTimeout("lightning()", 100); }
    if (flash == 2) { document.bgColor = 'red'; setTimeout("lightning()", 90); }
    if (flash == 3) { document.bgColor = 'crimson'; setTimeout("lightning()", 85); }
    if (flash == 4) { document.bgColor = 'white'; setTimeout("lightning()", 80); }
    if (flash == 5) { document.bgColor = 'orange'; setTimeout("lightning()", 75); }
    if (flash == 6) { document.bgColor = 'brown'; setTimeout("lightning()", 70); }
    if (flash == 7) { document.bgColor = 'white'; setTimeout("lightning()", 65); }
    if (flash == 8) { document.bgColor = 'gold'; setTimeout("lightning()", 60); }
    if (flash == 9) { document.bgColor = 'yellow'; setTimeout("lightning()", 50); }
    if (flash == 10) { document.bgColor = 'white'; setTimeout("lightning()", 40); }
    if (flash == 11) { document.bgColor = 'green'; setTimeout("lightning()", 30); }
    if (flash == 12) { document.bgColor = 'lightgreen'; setTimeout("lightning()", 25); }
    if (flash == 13) { document.bgColor = 'white'; setTimeout("lightning()", 20); }
    if (flash == 14) { document.bgColor = 'aqua'; setTimeout("lightning()", 10); }
    if (flash == 15) { document.bgColor = 'blue'; setTimeout("lightning()", 5); }
    if (flash == 16) { document.bgColor = 'white'; setTimeout("lightning()", 1); }
    if (flash == 17) { document.bgColor = 'purple'; setTimeout("lightning()", 1); }
    if (flash == 18) { document.bgColor = 'orchid'; setTimeout("lightning()", 1); }
    if (flash == 19) { document.bgColor = 'black'; setTimeout("lightning()", 1); }
    if (flash == 20) { flash = 0; setTimeout("lightning()", 100); }
}
setTimeout("lightning()", 1);