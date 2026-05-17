# Gemini Incident Context

Use this incident context to assess severity, likely incident type, what may be burning or affected, escalation risk, and recommended response. Treat the nearby-place data as evidence, not certainty.

```json
{
  "incident": {
    "id": "INC201",
    "reported_event_type": "FIRE",
    "latitude": 33.8938,
    "longitude": 35.5018,
    "reported_severity": 80.0
  },
  "nearby_context_radius_m": 200,
  "generic_unnamed_osm_summary": {
    "generic_unnamed_count": 28,
    "by_type": {
      "building:yes": 28
    },
    "within_50m": 0,
    "within_100m": 0,
    "within_200m": 28,
    "closest_distance_m": 110.73
  },
  "closest_recognizable_places": [
    {
      "name": "All Brands Factory Outlet",
      "source": "google",
      "distance_m": 1.32,
      "type": "discount_store",
      "role": "place",
      "address": "Tarik l matar, Bayrut, Lebanon",
      "lat": 33.8937882,
      "lon": 35.5017987,
      "google_place_id": "ChIJwQ5_5i8XHxUR6QM5akb_7eo"
    },
    {
      "name": "Beirut Badawi Modern Apartment",
      "source": "google",
      "distance_m": 1.98,
      "type": "lodging",
      "role": "place",
      "address": "Beirut, Lebanon",
      "lat": 33.8937912,
      "lon": 35.5017814,
      "google_place_id": "ChIJN9BOX-AWHxUR9AYgiTigARI"
    },
    {
      "name": "Beirut Spacious Loft",
      "source": "google",
      "distance_m": 1.98,
      "type": "lodging",
      "role": "place",
      "address": "Beirut, Lebanon",
      "lat": 33.8937912,
      "lon": 35.5017814,
      "google_place_id": "ChIJN9BOX-AWHxURTPnCce0PQlI"
    },
    {
      "name": "Boho 1 Mandala Studio W-24-24 Power in Mar Mikhael",
      "source": "google",
      "distance_m": 2.28,
      "type": "lodging",
      "role": "place",
      "address": "Beirut, Lebanon",
      "lat": 33.8937912,
      "lon": 35.5017777,
      "google_place_id": "ChIJfyxPX-AWHxURj5eEVfPflos"
    },
    {
      "name": "Mar Makhayel Studios",
      "source": "google",
      "distance_m": 2.28,
      "type": "lodging",
      "role": "place",
      "address": "Beirut, Lebanon",
      "lat": 33.8937912,
      "lon": 35.5017777,
      "google_place_id": "ChIJfyxPX-AWHxUROv2h9td8Axk"
    },
    {
      "name": "Seaview 602 1-BR Apartment by Gate 9 in Mar Mikhael",
      "source": "google",
      "distance_m": 2.28,
      "type": "lodging",
      "role": "place",
      "address": "Beirut, Lebanon",
      "lat": 33.8937912,
      "lon": 35.5017777,
      "google_place_id": "ChIJfyxPX-AWHxURY8qTLVjosdE"
    },
    {
      "name": "Iziingubo",
      "source": "google",
      "distance_m": 2.35,
      "type": "womens_clothing_store",
      "role": "place",
      "address": "Beirut 0000, Lebanon",
      "lat": 33.893791,
      "lon": 35.501777,
      "google_place_id": "ChIJhdzngG-aIEcRsqCdLFB4jf0"
    },
    {
      "name": "Ismod Lebanon, iQos Lebanon , Galaxy pro",
      "source": "google",
      "distance_m": 2.35,
      "type": "electronics_store",
      "role": "place",
      "address": "Street, tal3it yazbeck, بيروت، Lebanon",
      "lat": 33.893791,
      "lon": 35.501777,
      "google_place_id": "ChIJwVdrKG8XHxURq4SyBpWDuI8"
    },
    {
      "name": "SRDB LAW FIRM BEIRUT",
      "source": "google",
      "distance_m": 2.35,
      "type": "lawyer",
      "role": "place",
      "address": "26, 28 Badaro Street، Box : 116-2064، Bayrut, Lebanon",
      "lat": 33.893791,
      "lon": 35.501777,
      "google_place_id": "ChIJJy1PX-AWHxURAoWb5SSw7Gg"
    },
    {
      "name": "Housein Slim Photography",
      "source": "google",
      "distance_m": 2.35,
      "type": "service",
      "role": "place",
      "address": "Ain El Remmaneh, Lebanon",
      "lat": 33.893791,
      "lon": 35.501777,
      "google_place_id": "ChIJ_Y3tDwoXHxURwTO7GX3uIVE"
    },
    {
      "name": "International Paper Broker",
      "source": "google",
      "distance_m": 2.35,
      "type": "wholesaler",
      "role": "place",
      "address": "Rageb Harb، Haret Hreik, Lebanon",
      "lat": 33.893791,
      "lon": 35.501777,
      "google_place_id": "ChIJQzatjc4XHxURtguTTt_9gHg"
    },
    {
      "name": "Dawaer Foundation",
      "source": "google",
      "distance_m": 2.35,
      "type": "non_profit_organization",
      "role": "place",
      "address": "Forn El Chebbak, Lebanon",
      "lat": 33.893791,
      "lon": 35.501777,
      "google_place_id": "ChIJRRZIjCQXHxURsK65jMXWIMs"
    },
    {
      "name": "PRATEATO",
      "source": "google",
      "distance_m": 2.35,
      "type": "real_estate_agency",
      "role": "place",
      "address": "Foch Street, Marfaa 128 Building، FFA Real Estate, 4th Floor، Beirut Central District، Lebanon",
      "lat": 33.893791,
      "lon": 35.501777,
      "google_place_id": "ChIJJy1PX-AWHxURwJ4WG2QA7hs"
    },
    {
      "name": "Cyber Vision Solutions s.a.r.l",
      "source": "google",
      "distance_m": 2.35,
      "type": "service",
      "role": "place",
      "address": "Boulevard National, Bayrut 0000, Lebanon",
      "lat": 33.893791,
      "lon": 35.501777,
      "google_place_id": "ChIJGVr0nJ0_HxURFttaKfWisXs"
    },
    {
      "name": "Chaar Real Estate",
      "source": "google",
      "distance_m": 2.35,
      "type": "real_estate_agency",
      "role": "place",
      "address": "Mar Elias, Main, Facing Byblos Bank, 6th Floor, بيروت، Lebanon",
      "lat": 33.893791,
      "lon": 35.501777,
      "google_place_id": "ChIJue1_FawXHxUR1e2Cku9j99I"
    },
    {
      "name": "Gargour Asia Lebanon",
      "source": "google",
      "distance_m": 2.35,
      "type": "truck_dealer",
      "role": "place",
      "address": "Gallery semaan, Bayrut, Lebanon",
      "lat": 33.893791,
      "lon": 35.501777,
      "google_place_id": "ChIJh575YeRDHxUR8ugWc5aJEP4"
    },
    {
      "name": "TrainerMohammad.com",
      "source": "google",
      "distance_m": 2.35,
      "type": "google_place",
      "role": "place",
      "address": "Youssef El Assir Street، Shahine Building، 5th Floor، El Medawar House، Bayrut, Lebanon",
      "lat": 33.893791,
      "lon": 35.501777,
      "google_place_id": "ChIJV-pu3fUXHxUR3gwZwCrpjv8"
    },
    {
      "name": "Sky Lounge Services",
      "source": "google",
      "distance_m": 2.35,
      "type": "aircraft_rental_service",
      "role": "place",
      "address": "General Aviation Terminal, Rafic Hariri Int'l Airport, بيروت، Lebanon",
      "lat": 33.893791,
      "lon": 35.501777,
      "google_place_id": "ChIJw40kHNQXHxURGMRbgb1qq3s"
    },
    {
      "name": "صيدلية الظريف",
      "source": "google",
      "distance_m": 2.36,
      "type": "hospital",
      "role": "place",
      "address": "VGV2+GP6, Beirut, Lebanon",
      "lat": 33.8937912,
      "lon": 35.5017767,
      "google_place_id": "ChIJxSf1-CMXHxUR-pdsDbg_DbE"
    },
    {
      "name": "American Style Outlet",
      "source": "google",
      "distance_m": 2.36,
      "type": "shopping_mall",
      "role": "place",
      "address": "beirut barbour، بيروت،، Bayrut, Lebanon",
      "lat": 33.8937912,
      "lon": 35.5017767,
      "google_place_id": "ChIJk06KJ3QXHxUR7b8qWhVCcgk"
    },
    {
      "name": "UNESCO entrance",
      "source": "osm",
      "distance_m": 41.92,
      "type": "other",
      "role": "mapped_object",
      "address": null,
      "lat": 33.893952,
      "lon": 35.5022156,
      "osm_ref": "node/9495169395.0"
    },
    {
      "name": "Unnamed man_made:bridge",
      "source": "osm",
      "distance_m": 42.39,
      "type": "man_made:bridge",
      "role": "infrastructure",
      "address": null,
      "lat": 33.8934979,
      "lon": 35.5015198,
      "osm_ref": "way/778215955.0"
    },
    {
      "name": "Unnamed military:checkpoint",
      "source": "osm",
      "distance_m": 61.02,
      "type": "military:checkpoint",
      "role": "military",
      "address": null,
      "lat": 33.8941291,
      "lon": 35.502329,
      "osm_ref": "node/6497709288.0"
    },
    {
      "name": "No through road",
      "source": "osm",
      "distance_m": 100.34,
      "type": "amenity:police",
      "role": "place",
      "address": "شارع 21",
      "lat": 33.8929058,
      "lon": 35.501946,
      "osm_ref": "node/8100724617.0"
    },
    {
      "name": "United Nations Economic and Social Commission for Western Asia",
      "source": "osm",
      "distance_m": 100.67,
      "type": "office:diplomatic",
      "role": "place",
      "address": null,
      "lat": 33.8946793,
      "lon": 35.5020599,
      "osm_ref": "node/6069448586.0"
    },
    {
      "name": "Unnamed amenity:parking",
      "source": "osm",
      "distance_m": 101.56,
      "type": "amenity:parking",
      "role": "place",
      "address": null,
      "lat": 33.8941262,
      "lon": 35.5028278,
      "osm_ref": "way/546140448.0"
    },
    {
      "name": "Unnamed building",
      "source": "osm",
      "distance_m": 103.14,
      "type": "building:commercial",
      "role": "building",
      "address": null,
      "lat": 33.8946945,
      "lon": 35.5020955,
      "osm_ref": "way/483239204.0"
    },
    {
      "name": "National Evangelical Church of Beirut",
      "source": "osm",
      "distance_m": 111.53,
      "type": "amenity:place_of_worship",
      "role": "building",
      "address": "شارع أحمد الداعوق, بيروت",
      "lat": 33.8947526,
      "lon": 35.5014218,
      "osm_ref": "way/479475562.0"
    },
    {
      "name": "Phoenicia",
      "source": "osm",
      "distance_m": 115.81,
      "type": "amenity:fuel",
      "role": "place",
      "address": null,
      "lat": 33.8928411,
      "lon": 35.5022898,
      "osm_ref": "node/7417545305.0"
    },
    {
      "name": "Unnamed amenity:parking",
      "source": "osm",
      "distance_m": 128.62,
      "type": "amenity:parking",
      "role": "place",
      "address": null,
      "lat": 33.8943725,
      "lon": 35.5005892,
      "osm_ref": "way/438761510.0"
    },
    {
      "name": "Unnamed building",
      "source": "osm",
      "distance_m": 141.31,
      "type": "building:commercial",
      "role": "building",
      "address": null,
      "lat": 33.8950214,
      "lon": 35.502223,
      "osm_ref": "way/483239205.0"
    },
    {
      "name": "Unnamed amenity:parking",
      "source": "osm",
      "distance_m": 157.64,
      "type": "amenity:parking",
      "role": "place",
      "address": null,
      "lat": 33.8933609,
      "lon": 35.5034239,
      "osm_ref": "way/194545122.0"
    },
    {
      "name": "The Landmark",
      "source": "osm",
      "distance_m": 165.27,
      "type": "other",
      "role": "mapped_object",
      "address": null,
      "lat": 33.8946353,
      "lon": 35.503281,
      "osm_ref": "way/23856429.0"
    },
    {
      "name": "Rafiq Hariri",
      "source": "osm",
      "distance_m": 173.6,
      "type": "tourism:artwork",
      "role": "place",
      "address": null,
      "lat": 33.8952402,
      "lon": 35.501074,
      "osm_ref": "node/4815020860.0"
    },
    {
      "name": "Unnamed tourism:artwork",
      "source": "osm",
      "distance_m": 177.03,
      "type": "tourism:artwork",
      "role": "place",
      "address": null,
      "lat": 33.8950806,
      "lon": 35.5029396,
      "osm_ref": "node/4815020861.0"
    },
    {
      "name": "Unnamed amenity:parking",
      "source": "osm",
      "distance_m": 177.41,
      "type": "amenity:parking",
      "role": "place",
      "address": null,
      "lat": 33.8949634,
      "lon": 35.5031153,
      "osm_ref": "way/1180744514.0"
    },
    {
      "name": "Place Riad El-Solh",
      "source": "osm",
      "distance_m": 179.17,
      "type": "other",
      "role": "mapped_object",
      "address": null,
      "lat": 33.8950857,
      "lon": 35.50297,
      "osm_ref": "way/34380915.0"
    }
  ],
  "risk_relevant_places": [
    {
      "name": "Boho 1 Mandala Studio W-24-24 Power in Mar Mikhael",
      "source": "google",
      "distance_m": 2.28,
      "type": "lodging",
      "role": "place",
      "address": "Beirut, Lebanon",
      "lat": 33.8937912,
      "lon": 35.5017777,
      "google_place_id": "ChIJfyxPX-AWHxURj5eEVfPflos"
    },
    {
      "name": "United Nations Economic and Social Commission for Western Asia",
      "source": "osm",
      "distance_m": 100.67,
      "type": "office:diplomatic",
      "role": "place",
      "address": null,
      "lat": 33.8946793,
      "lon": 35.5020599,
      "osm_ref": "node/6069448586.0"
    },
    {
      "name": "National Evangelical Church of Beirut",
      "source": "osm",
      "distance_m": 111.53,
      "type": "amenity:place_of_worship",
      "role": "building",
      "address": "شارع أحمد الداعوق, بيروت",
      "lat": 33.8947526,
      "lon": 35.5014218,
      "osm_ref": "way/479475562.0"
    },
    {
      "name": "All Brands Factory Outlet",
      "source": "google",
      "distance_m": 1.32,
      "type": "discount_store",
      "role": "place",
      "address": "Tarik l matar, Bayrut, Lebanon",
      "lat": 33.8937882,
      "lon": 35.5017987,
      "google_place_id": "ChIJwQ5_5i8XHxUR6QM5akb_7eo"
    },
    {
      "name": "Beirut Badawi Modern Apartment",
      "source": "google",
      "distance_m": 1.98,
      "type": "lodging",
      "role": "place",
      "address": "Beirut, Lebanon",
      "lat": 33.8937912,
      "lon": 35.5017814,
      "google_place_id": "ChIJN9BOX-AWHxUR9AYgiTigARI"
    },
    {
      "name": "Beirut Spacious Loft",
      "source": "google",
      "distance_m": 1.98,
      "type": "lodging",
      "role": "place",
      "address": "Beirut, Lebanon",
      "lat": 33.8937912,
      "lon": 35.5017814,
      "google_place_id": "ChIJN9BOX-AWHxURTPnCce0PQlI"
    },
    {
      "name": "Mar Makhayel Studios",
      "source": "google",
      "distance_m": 2.28,
      "type": "lodging",
      "role": "place",
      "address": "Beirut, Lebanon",
      "lat": 33.8937912,
      "lon": 35.5017777,
      "google_place_id": "ChIJfyxPX-AWHxUROv2h9td8Axk"
    },
    {
      "name": "Seaview 602 1-BR Apartment by Gate 9 in Mar Mikhael",
      "source": "google",
      "distance_m": 2.28,
      "type": "lodging",
      "role": "place",
      "address": "Beirut, Lebanon",
      "lat": 33.8937912,
      "lon": 35.5017777,
      "google_place_id": "ChIJfyxPX-AWHxURY8qTLVjosdE"
    },
    {
      "name": "صيدلية الظريف",
      "source": "google",
      "distance_m": 2.36,
      "type": "hospital",
      "role": "place",
      "address": "VGV2+GP6, Beirut, Lebanon",
      "lat": 33.8937912,
      "lon": 35.5017767,
      "google_place_id": "ChIJxSf1-CMXHxUR-pdsDbg_DbE"
    },
    {
      "name": "Unnamed man_made:bridge",
      "source": "osm",
      "distance_m": 42.39,
      "type": "man_made:bridge",
      "role": "infrastructure",
      "address": null,
      "lat": 33.8934979,
      "lon": 35.5015198,
      "osm_ref": "way/778215955.0"
    },
    {
      "name": "Unnamed military:checkpoint",
      "source": "osm",
      "distance_m": 61.02,
      "type": "military:checkpoint",
      "role": "military",
      "address": null,
      "lat": 33.8941291,
      "lon": 35.502329,
      "osm_ref": "node/6497709288.0"
    },
    {
      "name": "No through road",
      "source": "osm",
      "distance_m": 100.34,
      "type": "amenity:police",
      "role": "place",
      "address": "شارع 21",
      "lat": 33.8929058,
      "lon": 35.501946,
      "osm_ref": "node/8100724617.0"
    },
    {
      "name": "Unnamed amenity:parking",
      "source": "osm",
      "distance_m": 101.56,
      "type": "amenity:parking",
      "role": "place",
      "address": null,
      "lat": 33.8941262,
      "lon": 35.5028278,
      "osm_ref": "way/546140448.0"
    },
    {
      "name": "Phoenicia",
      "source": "osm",
      "distance_m": 115.81,
      "type": "amenity:fuel",
      "role": "place",
      "address": null,
      "lat": 33.8928411,
      "lon": 35.5022898,
      "osm_ref": "node/7417545305.0"
    },
    {
      "name": "Unnamed amenity:parking",
      "source": "osm",
      "distance_m": 128.62,
      "type": "amenity:parking",
      "role": "place",
      "address": null,
      "lat": 33.8943725,
      "lon": 35.5005892,
      "osm_ref": "way/438761510.0"
    },
    {
      "name": "Unnamed amenity:parking",
      "source": "osm",
      "distance_m": 157.64,
      "type": "amenity:parking",
      "role": "place",
      "address": null,
      "lat": 33.8933609,
      "lon": 35.5034239,
      "osm_ref": "way/194545122.0"
    },
    {
      "name": "Unnamed amenity:parking",
      "source": "osm",
      "distance_m": 177.41,
      "type": "amenity:parking",
      "role": "place",
      "address": null,
      "lat": 33.8949634,
      "lon": 35.5031153,
      "osm_ref": "way/1180744514.0"
    }
  ],
  "required_llm_output": {
    "severity": "low | medium | high | critical",
    "incident_type": "residential_fire | commercial_fire | industrial_fire | fuel_fire | electrical_fire | vehicle_fire | explosion | earthquake | unknown",
    "what_is_likely_burning": "short explanation based on incident and nearby context",
    "potential_escalation": "short escalation assessment",
    "nearby_risks": [
      "list of specific nearby places or categories that matter"
    ],
    "recommended_response": {
      "fire_units": "integer",
      "ambulances": "integer",
      "police_required": "boolean",
      "special_units": [
        "hazmat",
        "rescue",
        "evacuation_support"
      ]
    },
    "confidence": "0.0 to 1.0",
    "reasoning_summary": "brief evidence-based explanation",
    "data_gaps": [
      "missing or uncertain information"
    ]
  }
}
```
