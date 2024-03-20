# get data for moment.js
def update(tz, out):
	ltz = data["links"].get(tz, tz)
	zone = data["zones"].get(ltz)
	if not zone:
		return

	out["zones"][ltz] = zone
	out["links"][tz] = ltz
	for z in zone:
		parts = z.split(" ")
		if parts[1] in data["rules"]:
			out["rules"][parts[1]] = data["rules"][parts[1]]


def get_all_timezones():
	return sorted(list(data["zones"]))


data = {
	"zones": {
		"Asia/Ho_Chi_Minh": [
			"7:6:40 - LMT 1906_5_9 7:6:40",
			"7:6:20 - SMT 1911_2_11_0_1 7:6:20",
			"7 - ICT 1912_4 7",
			"8 - ICT 1931_4 8",
			"7 - ICT",
		]
	},
	"rules": {},
	"links": {},
}
