package com.example.django_project;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.Bundle;

//import android.support.v7.app.AppCompatActivity;
//import android.os.Bundle;


import android.util.Log;

import java.io.File;
import java.net.URI;

import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;


public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        uploadFoto();
    }

    private void uploadFoto() {

        System.out.println("..............i am here.......");
       String image_path = "/storage/emulated/0/Download/d68a4a642374fe6e127ff7b39b37d7ae.png";
        Uri path1 = Uri.parse("android.resource://"+BuildConfig.APPLICATION_ID+"/"+R.drawable.truck);
        //String image_path = path1.getPath();
        Bitmap image=BitmapFactory.decodeFile("file://android_asset/image/truck.png");

        File imageFile = new File(image_path);


        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl(DjangoApi.DJANGO_SITE)
                .addConverterFactory(GsonConverterFactory.create())
                .build();


        DjangoApi postApi= retrofit.create(DjangoApi.class);


        RequestBody requestBody = RequestBody.create(MediaType.parse("multipart/data"), imageFile);
        MultipartBody.Part multiPartBody = MultipartBody.Part
                .createFormData("model_pic", imageFile.getName(), requestBody);



        Call<RequestBody> call = postApi.uploadFile(multiPartBody);

        call.enqueue(new Callback<RequestBody>() {
            @Override
            public void onResponse(Call<RequestBody> call, Response<RequestBody> response) {
                Log.d("good", "good");
                System.out.println("......okay done.............");

            }
            @Override
            public void onFailure(Call<RequestBody> call, Throwable t) {
                Log.d("fail", "fail"+t);
            }
        });


    }

}

