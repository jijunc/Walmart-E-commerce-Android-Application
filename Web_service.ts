private void getProductInfo(String productId) {
    // Build the URL for the Walmart API request
    String apiUrl = "https://api.walmart.com/product/" + productId + "?apiKey=<your_api_key>";
    
    // Create a request queue for Volley to handle network requests
    RequestQueue queue = Volley.newRequestQueue(this);
    
    // Send the API request
    JsonObjectRequest request = new JsonObjectRequest(Request.Method.GET, apiUrl, null,
        new Response.Listener<JSONObject>() {
            @Override
            public void onResponse(JSONObject response) {
                // Parse the product information from the API response
                String productName = response.optString("productName");
                String productDescription = response.optString("shortDescription");
                double productPrice = response.optDouble("price");
                String productImage = response.optString("productImageUrl");
                
                // Update the UI with the product information
                productNameTextView.setText(productName);
                productDescriptionTextView.setText(productDescription);
                productPriceTextView.setText(String.format("$%.2f", productPrice));
                Glide.with(ProductActivity.this).load(productImage).into(productImageView);
            }
        },
        new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                // Handle API request error
                Log.e(TAG, "API request error: " + error.getMessage());
            }
        });
    queue.add(request);
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////

private void createProduct(String productName, String productDescription, double productPrice, String productImage) {
    // Build the URL for the Walmart API request
    String apiUrl = "https://api.walmart.com/product";
    
    // Create a request queue for Volley to handle network requests
    RequestQueue queue = Volley.newRequestQueue(this);
    
    // Create the JSON payload for the POST request
    JSONObject payload = new JSONObject();
    try {
        payload.put("productName", productName);
        payload.put("shortDescription", productDescription);
        payload.put("price", productPrice);
        payload.put("productImageUrl", productImage);
    } catch (JSONException e) {
        e.printStackTrace();
    }
    
    // Send the POST request
    JsonObjectRequest request = new JsonObjectRequest(Request.Method.POST, apiUrl, payload,
        new Response.Listener<JSONObject>() {
            @Override
            public void onResponse(JSONObject response) {
                // Handle successful POST request response
                Log.d(TAG, "Product created: " + response.toString());
            }
        },
        new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                // Handle POST request error
                Log.e(TAG, "POST request error: " + error.getMessage());
            }
        });
    queue.add(request);
}
