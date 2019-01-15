<?php

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It is a breeze. Simply tell Lumen the URIs it should respond to
| and give it the Closure to call when that URI is requested.
|
*/

$router->get('/', function () use ($router) {
    return "Welcome to JAM the house!";
});

$router->group(['prefix' => 'api/v1/{letter}'], function () use ($router) {
    $router->get('status', function($letter) {
        $letter = sanitizeLetter($letter);

        $command = escapeshellcmd(getcwd() . '/../scripts/jam.py status ' . $letter);
        $status = shell_exec($command);

        return $status;
    });

    $router->post('toggle', function($letter) {
        $letter = sanitizeLetter($letter);

        $command = escapeshellcmd(getcwd() . '/../scripts/jam.py toggle ' . $letter);
        $status = shell_exec($command);

        return $status;
    });

    $router->post('on', function($letter) {
        $letter = sanitizeLetter($letter);

        $command = escapeshellcmd(getcwd() . '/../scripts/jam.py open ' . $letter);
        $status = shell_exec($command);

        return $status;
    });

    $router->post('off', function($letter) {
        $letter = sanitizeLetter($letter);

        $command = escapeshellcmd(getcwd() . '/../scripts/jam.py close ' . $letter);
        $status = shell_exec($command);

        return $status;
    });
});
