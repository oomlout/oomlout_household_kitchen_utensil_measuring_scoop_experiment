$fn = 50;


difference() {
	union() {
		translate(v = [-23.8966182896, 0, 0]) {
			hull() {
				translate(v = [-16.8966182896, 0.0000000000, 0]) {
					cylinder(h = 12.5000000000, r = 12);
				}
				translate(v = [16.8966182896, 0.0000000000, 0]) {
					cylinder(h = 12.5000000000, r = 12);
				}
				translate(v = [-16.8966182896, 0.0000000000, 0]) {
					cylinder(h = 12.5000000000, r = 12);
				}
				translate(v = [16.8966182896, 0.0000000000, 0]) {
					cylinder(h = 12.5000000000, r = 12);
				}
			}
		}
		translate(v = [8.1006465957, 0, 0]) {
			hull() {
				translate(v = [-19.1006465957, 0.0000000000, 0]) {
					cylinder(h = 9.5000000000, r = 9);
				}
				translate(v = [19.1006465957, 0.0000000000, 0]) {
					cylinder(h = 9.5000000000, r = 9);
				}
				translate(v = [-19.1006465957, 0.0000000000, 0]) {
					cylinder(h = 9.5000000000, r = 9);
				}
				translate(v = [19.1006465957, 0.0000000000, 0]) {
					cylinder(h = 9.5000000000, r = 9);
				}
			}
		}
	}
	union() {
		translate(v = [20.1006465957, 0, 1.5000000000]) {
			#hull() {
				union() {
					translate(v = [-7.1006465957, 0.0000000000, 8]) {
						cylinder(h = 0, r = 8);
					}
					translate(v = [-7.1006465957, 0.0000000000, 8]) {
						sphere(r = 8);
					}
					translate(v = [-7.1006465957, 0.0000000000, 8]) {
						sphere(r = 8);
					}
				}
				union() {
					translate(v = [7.1006465957, 0.0000000000, 8]) {
						cylinder(h = 0, r = 8);
					}
					translate(v = [7.1006465957, 0.0000000000, 8]) {
						sphere(r = 8);
					}
					translate(v = [7.1006465957, 0.0000000000, 8]) {
						sphere(r = 8);
					}
				}
				union() {
					translate(v = [-7.1006465957, 0.0000000000, 8]) {
						cylinder(h = 0, r = 8);
					}
					translate(v = [-7.1006465957, 0.0000000000, 8]) {
						sphere(r = 8);
					}
					translate(v = [-7.1006465957, 0.0000000000, 8]) {
						sphere(r = 8);
					}
				}
				union() {
					translate(v = [7.1006465957, 0.0000000000, 8]) {
						cylinder(h = 0, r = 8);
					}
					translate(v = [7.1006465957, 0.0000000000, 8]) {
						sphere(r = 8);
					}
					translate(v = [7.1006465957, 0.0000000000, 8]) {
						sphere(r = 8);
					}
				}
			}
		}
		translate(v = [-28.3966182896, 0, 1.5000000000]) {
			#hull() {
				union() {
					translate(v = [-12.3966182896, 0.0000000000, 11]) {
						cylinder(h = 0, r = 11);
					}
					translate(v = [-12.3966182896, 0.0000000000, 11]) {
						sphere(r = 11);
					}
					translate(v = [-12.3966182896, 0.0000000000, 11]) {
						sphere(r = 11);
					}
				}
				union() {
					translate(v = [12.3966182896, 0.0000000000, 11]) {
						cylinder(h = 0, r = 11);
					}
					translate(v = [12.3966182896, 0.0000000000, 11]) {
						sphere(r = 11);
					}
					translate(v = [12.3966182896, 0.0000000000, 11]) {
						sphere(r = 11);
					}
				}
				union() {
					translate(v = [-12.3966182896, 0.0000000000, 11]) {
						cylinder(h = 0, r = 11);
					}
					translate(v = [-12.3966182896, 0.0000000000, 11]) {
						sphere(r = 11);
					}
					translate(v = [-12.3966182896, 0.0000000000, 11]) {
						sphere(r = 11);
					}
				}
				union() {
					translate(v = [12.3966182896, 0.0000000000, 11]) {
						cylinder(h = 0, r = 11);
					}
					translate(v = [12.3966182896, 0.0000000000, 11]) {
						sphere(r = 11);
					}
					translate(v = [12.3966182896, 0.0000000000, 11]) {
						sphere(r = 11);
					}
				}
			}
		}
		#translate(v = [0, 0, -100.0000000000]) {
			cylinder(h = 200, r = 3.2500000000);
		}
	}
}